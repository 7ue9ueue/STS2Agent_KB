"""MCP server bridge for Slay the Spire 2.

Connects to the STS2_MCP mod's HTTP server and exposes game actions
as MCP tools for Claude Desktop / Claude Code.
"""

import argparse
import asyncio
import inspect
import json
import os
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sts2")

_base_url: str = "http://localhost:15526"
_trust_env: bool = True
_repo_root = Path(__file__).resolve().parent.parent
_log_enabled = os.environ.get("STS2_TOOL_LOG", "").lower() in {"1", "true", "yes", "on"}
_log_session_id = os.environ.get("STS2_TOOL_LOG_SESSION") or (
    datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:8]
)
_log_local_run = os.environ.get("STS2_TOOL_LOG_RUN")
_log_run_id = os.environ.get("STS2_TOOL_LOG_RUN_ID")
_log_seq = 0
_log_lock = asyncio.Lock()
_log_path_env = os.environ.get("STS2_TOOL_LOG_PATH")
_log_file_stem = _log_local_run or _log_run_id or f"sts2_tool_log_{_log_session_id}"
_log_path = (
    Path(_log_path_env).expanduser()
    if _log_path_env
    else _repo_root / "history" / "tool_logs" / f"{_log_file_stem}.jsonl"
)
_max_response_bytes = int(os.environ.get("STS2_TOOL_LOG_MAX_RESPONSE_BYTES", "0") or "0")
_max_request_bytes = int(os.environ.get("STS2_TOOL_LOG_MAX_REQUEST_BYTES", "0") or "0")
_log_detail = os.environ.get("STS2_TOOL_LOG_DETAIL", "full").lower()


def _safe_log_stem(value: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip())
    stem = stem.strip(".")
    if not stem:
        raise ValueError("Log run name must contain at least one safe filename character")
    if stem in {".", ".."}:
        raise ValueError("Invalid log run name")
    return stem


def _default_log_path_for(local_run: str | None, run_id: str | None) -> Path:
    raw_stem = local_run or run_id or f"sts2_tool_log_{_log_session_id}"
    return _repo_root / "history" / "tool_logs" / f"{_safe_log_stem(raw_stem)}.jsonl"


def _sp_url() -> str:
    return f"{_base_url}/api/v1/singleplayer"


def _mp_url() -> str:
    return f"{_base_url}/api/v1/multiplayer"


def _profile_url() -> str:
    return f"{_base_url}/api/v1/profile"


def _profiles_url() -> str:
    return f"{_base_url}/api/v1/profiles"


def _truncate_text(value: str | None, max_bytes: int) -> dict | str | None:
    if value is None or max_bytes <= 0:
        return value

    raw = value.encode("utf-8")
    if len(raw) <= max_bytes:
        return value

    truncated = raw[:max_bytes].decode("utf-8", errors="replace")
    return {
        "truncated": True,
        "bytes": len(raw),
        "max_bytes": max_bytes,
        "text": truncated,
    }


def _truncate_json(value: object, max_bytes: int) -> object:
    if max_bytes <= 0:
        return value

    try:
        text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    except TypeError:
        text = repr(value)

    return _truncate_text(text, max_bytes)


def _infer_tool_name() -> str | None:
    helper_names = {
        "_infer_tool_name",
        "_log_http_event",
        "_request_text",
        "_get",
        "_post",
        "_mp_get",
        "_mp_post",
        "_profile_get",
        "_profiles_get",
        "_profiles_post",
        "_wait_for_profile",
    }
    for frame in inspect.stack()[2:]:
        name = frame.function
        if name.startswith("_") or name in helper_names:
            continue
        return name
    return None


def _name_or_id(item: object) -> object:
    if not isinstance(item, dict):
        return item
    return item.get("name") or item.get("id") or item


def _power_summary(power: object) -> object:
    if not isinstance(power, dict):
        return power
    name = power.get("name") or power.get("id")
    amount = power.get("amount")
    if amount is None:
        amount = power.get("stacks")
    if amount is None:
        return name
    return {"name": name, "amount": amount}


def _card_summary(card: object) -> object:
    if not isinstance(card, dict):
        return card

    summary = {
        key: card.get(key)
        for key in (
            "index",
            "name",
            "id",
            "type",
            "cost",
            "is_upgraded",
            "can_play",
            "unplayable_reason",
        )
        if key in card
    }
    if "is_upgraded" in summary:
        summary["upgraded"] = summary.pop("is_upgraded")
    return summary


def _relic_summary(relic: object) -> object:
    if not isinstance(relic, dict):
        return relic
    summary = {"name": relic.get("name") or relic.get("id")}
    if relic.get("counter") is not None:
        summary["counter"] = relic.get("counter")
    return summary


def _potion_summary(potion: object) -> object:
    if not isinstance(potion, dict):
        return potion
    return {
        key: potion.get(key)
        for key in ("slot", "name", "id", "target_type", "can_use_in_combat")
        if key in potion
    }


def _enemy_summary(enemy: object) -> object:
    if not isinstance(enemy, dict):
        return enemy

    summary = {
        key: enemy.get(key)
        for key in (
            "entity_id",
            "name",
            "hp",
            "max_hp",
            "block",
            "intent",
            "intent_damage",
            "intent_hits",
        )
        if key in enemy
    }
    if "status" in enemy:
        summary["status"] = [_power_summary(power) for power in enemy.get("status", [])]
    return summary


def _option_summary(option: object) -> object:
    if not isinstance(option, dict):
        return option
    return {
        key: option.get(key)
        for key in (
            "index",
            "id",
            "name",
            "type",
            "label",
            "text",
            "description",
            "disabled",
            "node_type",
            "x",
            "y",
            "col",
            "row",
            "boss_id",
        )
        if key in option
    }


def _player_summary(player: object) -> object:
    if not isinstance(player, dict):
        return player

    summary = {
        key: player.get(key)
        for key in (
            "character",
            "hp",
            "max_hp",
            "block",
            "gold",
            "energy",
            "max_energy",
            "stars",
        )
        if key in player
    }
    if "status" in player:
        summary["status"] = [_power_summary(power) for power in player.get("status", [])]
    if "relics" in player:
        summary["relics"] = [_relic_summary(relic) for relic in player.get("relics", [])]
    if "potions" in player:
        summary["potions"] = [_potion_summary(potion) for potion in player.get("potions", [])]
    if "hand" in player:
        summary["hand"] = [_card_summary(card) for card in player.get("hand", [])]
    for pile in ("draw_pile", "discard_pile", "exhaust_pile", "deck"):
        if pile in player and isinstance(player[pile], list):
            summary[f"{pile}_count"] = len(player[pile])
    return summary


def _summarize_json_state(state: dict) -> dict:
    summary = {
        key: state.get(key)
        for key in (
            "state_type",
            "game_mode",
            "menu_screen",
            "message",
            "net_type",
            "player_count",
            "local_player_slot",
        )
        if key in state
    }
    if "run" in state:
        summary["run"] = state.get("run")
    if "player" in state:
        summary["player"] = _player_summary(state.get("player"))
    if "players" in state:
        summary["players"] = [_player_summary(player) for player in state.get("players", [])]

    battle = state.get("battle")
    if isinstance(battle, dict):
        summary["battle"] = {
            key: battle.get(key)
            for key in ("round", "turn", "is_play_phase", "all_players_ready")
            if key in battle
        }
        if "enemies" in battle:
            summary["battle"]["enemies"] = [_enemy_summary(enemy) for enemy in battle.get("enemies", [])]

    for screen_key in ("card_select", "hand_select", "card_reward"):
        screen = state.get(screen_key)
        if isinstance(screen, dict):
            compact = {
                key: screen.get(key)
                for key in (
                    "screen_type",
                    "prompt",
                    "preview_showing",
                    "can_cancel",
                    "can_confirm",
                )
                if key in screen
            }
            if "cards" in screen:
                compact["cards"] = [_card_summary(card) for card in screen.get("cards", [])]
            summary[screen_key] = compact

    for screen_key in ("map", "event", "shop", "fake_merchant", "rest", "rewards", "treasure"):
        screen = state.get(screen_key)
        if not isinstance(screen, dict):
            continue
        compact = {
            key: screen.get(key)
            for key in (
                "name",
                "event_id",
                "prompt",
                "is_shared",
                "all_voted",
                "all_bid",
                "is_bidding_phase",
            )
            if key in screen
        }
        for list_key in ("options", "next_options", "items", "rewards", "relics", "votes", "bids"):
            if list_key in screen and isinstance(screen[list_key], list):
                compact[list_key] = [_option_summary(item) for item in screen[list_key]]
        summary[screen_key] = compact

    return summary


def _summarize_markdown_state(text: str) -> dict:
    kept_lines = []
    skip_prefixes = ("  Future paths:", "- **Injury**:", "- **Unplayable**:")
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(skip_prefixes):
            continue
        if (
            stripped.startswith("#")
            or stripped.startswith("**Act ")
            or stripped.startswith("**The ")
            or stripped.startswith("- [")
            or stripped.startswith("- **")
            or stripped.startswith("## ")
        ):
            kept_lines.append(stripped)
        if len(kept_lines) >= 80:
            break
    return {"format": "markdown", "lines": kept_lines}


def _should_summarize_response(scope: str, method: str) -> bool:
    return _log_detail in {"summary", "thin"} and method == "GET" and scope in {"singleplayer", "multiplayer"}


def _summarize_response_text(text: str) -> dict:
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return _summarize_markdown_state(text)

    if isinstance(parsed, dict):
        return _summarize_json_state(parsed)
    return {"value": parsed}


async def _log_http_event(event: dict) -> None:
    if not _log_enabled:
        return

    global _log_seq
    async with _log_lock:
        _log_seq += 1
        event["seq"] = _log_seq
        event["session_id"] = _log_session_id
        if _log_local_run:
            event["local_run"] = _log_local_run
        if _log_run_id:
            event["run_id"] = _log_run_id
        event.setdefault("ts", datetime.now(timezone.utc).isoformat())

        try:
            _log_path.parent.mkdir(parents=True, exist_ok=True)
            with _log_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")
        except Exception as e:
            print(f"STS2 tool logger error: {e}", file=sys.stderr)


async def _request_text(
    *,
    scope: str,
    method: str,
    url: str,
    params: dict | None = None,
    body: dict | None = None,
) -> str:
    tool_name = _infer_tool_name() if _log_enabled else None
    started = time.perf_counter()
    event = {
        "tool": tool_name,
        "scope": scope,
        "method": method,
        "url": url,
        "params": _truncate_json(params, _max_request_bytes),
        "request": _truncate_json(body, _max_request_bytes),
    }

    try:
        async with httpx.AsyncClient(timeout=10, trust_env=_trust_env) as client:
            if method == "GET":
                r = await client.get(url, params=params)
            elif method == "POST":
                r = await client.post(url, json=body)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response_text = r.text
            ok = 200 <= r.status_code < 400
            response_log: dict
            if ok and _should_summarize_response(scope, method):
                response_log = {
                    "response_summary": _summarize_response_text(response_text),
                    "response_bytes": len(response_text.encode("utf-8")),
                }
            else:
                response_log = {
                    "response": _truncate_text(response_text, _max_response_bytes),
                }
            event.update(
                {
                    "ok": ok,
                    "status_code": r.status_code,
                    "duration_ms": round((time.perf_counter() - started) * 1000, 3),
                    **response_log,
                }
            )
            if not ok:
                event["error_type"] = "HTTPStatusError"
                event["error"] = f"HTTP {r.status_code}"
            await _log_http_event(event)
            r.raise_for_status()
            return response_text
    except Exception as e:
        if isinstance(e, httpx.HTTPStatusError):
            raise

        event.update(
            {
                "ok": False,
                "duration_ms": round((time.perf_counter() - started) * 1000, 3),
                "error_type": type(e).__name__,
                "error": str(e),
            }
        )
        await _log_http_event(event)
        raise


def _print_log_startup_message() -> None:
    if _log_enabled:
        print(f"STS2 tool logging enabled: {_log_path}", file=sys.stderr)


async def _get(params: dict | None = None) -> str:
    return await _request_text(scope="singleplayer", method="GET", url=_sp_url(), params=params)


async def _post(body: dict) -> str:
    return await _request_text(scope="singleplayer", method="POST", url=_sp_url(), body=body)


async def _mp_get(params: dict | None = None) -> str:
    return await _request_text(scope="multiplayer", method="GET", url=_mp_url(), params=params)


async def _mp_post(body: dict) -> str:
    return await _request_text(scope="multiplayer", method="POST", url=_mp_url(), body=body)


async def _profile_get() -> str:
    return await _request_text(scope="profile", method="GET", url=_profile_url())


async def _profiles_get() -> str:
    return await _request_text(scope="profiles", method="GET", url=_profiles_url())


async def _profiles_post(body: dict) -> str:
    return await _request_text(scope="profiles", method="POST", url=_profiles_url(), body=body)


async def _wait_for_profile(profile_id: int, fallback: str) -> str:
    last_profiles: dict | None = None
    for _ in range(30):
        await asyncio.sleep(0.1)
        profiles_text = await _profiles_get()
        profiles = json.loads(profiles_text)
        last_profiles = profiles
        if profiles.get("current_profile_id") == profile_id:
            return json.dumps(
                {
                    "status": "ok",
                    "message": f"Switched to profile {profile_id}",
                    "current_profile_id": profile_id,
                    "profiles": profiles.get("profiles", []),
                },
                indent=2,
            )

    return json.dumps(
        {
            "status": "error",
            "error": f"Timed out waiting for profile {profile_id} to become active",
            "current_profile_id": (
                last_profiles.get("current_profile_id")
                if isinstance(last_profiles, dict)
                else None
            ),
            "profiles": (
                last_profiles.get("profiles", [])
                if isinstance(last_profiles, dict)
                else []
            ),
            "initial_response": fallback,
        },
        indent=2,
    )


def _handle_error(e: Exception) -> str:
    if isinstance(e, httpx.ConnectError):
        return "Error: Cannot connect to STS2_MCP mod. Is the game running with the mod enabled?"
    if isinstance(e, httpx.HTTPStatusError):
        return f"Error: HTTP {e.response.status_code} — {e.response.text}"
    return f"Error: {e}"


async def _set_tool_log_target(local_run: str, run_id: str | None = None) -> dict:
    safe_local_run = _safe_log_stem(local_run)
    safe_run_id = _safe_log_stem(run_id) if run_id else None

    global _log_enabled, _log_local_run, _log_run_id, _log_file_stem, _log_path
    _log_enabled = True
    _log_local_run = safe_local_run
    _log_run_id = safe_run_id
    _log_file_stem = safe_local_run
    _log_path = _default_log_path_for(_log_local_run, _log_run_id)

    result = {
        "status": "ok",
        "message": f"Tool transcript logging is now paired with {safe_local_run}",
        "enabled": _log_enabled,
        "local_run": _log_local_run,
        "run_id": _log_run_id,
        "path": str(_log_path),
            "session_id": _log_session_id,
            "detail": _log_detail,
        }
    await _log_http_event(
        {
            "tool": "set_tool_log_run",
            "scope": "logger",
            "method": "CONFIG",
            "ok": True,
            "status_code": None,
            "duration_ms": 0,
            "request": {"local_run": local_run, "run_id": run_id},
            "response": json.dumps(result, ensure_ascii=False, separators=(",", ":")),
        }
    )
    return result


def _set_log_detail(detail: str) -> dict:
    normalized = detail.lower().strip()
    if normalized not in {"full", "summary", "thin"}:
        raise ValueError("detail must be one of: full, summary, thin")

    global _log_detail
    _log_detail = normalized
    return {
        "status": "ok",
        "message": f"Tool transcript detail is now {normalized}",
        "detail": _log_detail,
        "path": str(_log_path),
        "session_id": _log_session_id,
    }


# ---------------------------------------------------------------------------
# General
# ---------------------------------------------------------------------------


@mcp.tool()
async def set_tool_log_run(local_run: str, run_id: str | None = None) -> str:
    """Set the active tool transcript log target for the current local run.

    Use this at the start of a run after creating history/run<N>.md so the
    logger writes subsequent tool transcripts to history/tool_logs/run<N>.jsonl.

    Args:
        local_run: Local history run key, e.g. "run20".
        run_id: Optional secondary run id to include in events.
    """
    try:
        return json.dumps(await _set_tool_log_target(local_run, run_id), indent=2)
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def get_tool_log_status() -> str:
    """Get the current MCP tool transcript logging target."""
    return json.dumps(
        {
            "enabled": _log_enabled,
            "local_run": _log_local_run,
            "run_id": _log_run_id,
            "path": str(_log_path),
            "session_id": _log_session_id,
            "max_response_bytes": _max_response_bytes,
            "max_request_bytes": _max_request_bytes,
            "detail": _log_detail,
        },
        indent=2,
    )


@mcp.tool()
async def set_tool_log_detail(detail: str) -> str:
    """Set transcript detail mode at runtime.

    Args:
        detail: "full" for raw responses, or "summary"/"thin" for compact
            singleplayer/multiplayer get_game_state responses.
    """
    try:
        return json.dumps(_set_log_detail(detail), indent=2)
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def get_game_state(format: str = "markdown") -> str:
    """Get the current Slay the Spire 2 game state.

    Returns the full game state including player stats, hand, enemies, potions, etc.
    The state_type field indicates the current screen (combat, map, event, shop,
    fake_merchant, etc.).

    Args:
        format: "markdown" for human-readable output, "json" for structured data.
    """
    try:
        return await _get({"format": format})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def menu_select(option: str, seed: str | None = None) -> str:
    """Select a visible menu option.

    Use with state_type "menu" or "game_over". Supports main-menu navigation,
    singleplayer and multiplayer submenus, character select, timeline controls,
    tutorial prompts, and game-over main-menu return.

    Args:
        option: Option ID from the current menu state's options list. If an
            option is listed under blocked_options, selecting it returns the
            API's manual-action response instead of forcing UI entry.
        seed: Optional seed for supported embark flows. Standard mode rejects seeds.
    """
    body: dict = {"action": "menu_select", "option": option}
    if seed is not None:
        body["seed"] = seed
    try:
        return await _post(body)
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def save_and_quit() -> str:
    """Save the current singleplayer run and return to the main menu.

    Uses the game's in-run pause menu Save and Quit control. If the pause menu
    has to be opened asynchronously, call the tool again after a short delay.
    """
    try:
        return await _post({"action": "save_and_quit"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def get_profile() -> str:
    """Get the current profile's persistent progress summary.

    Includes character stats, discovered content, achievements, epochs, and global
    run totals for the active profile.
    """
    try:
        return await _profile_get()
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def list_profiles() -> str:
    """List the three profile slots and identify the active slot.

    The has_data field indicates whether a slot currently has progress data.
    """
    try:
        return await _profiles_get()
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def switch_profile(profile_id: int) -> str:
    """Switch to a profile slot through the game's profile UI.

    Use an empty slot to create or enter a fresh profile for testing. This cannot
    be used while a run is in progress.

    Args:
        profile_id: Profile slot to switch to. Must be 1, 2, or 3.
    """
    try:
        body = {"action": "switch", "profile_id": profile_id}
        result = await _profiles_post(body)
        try:
            parsed = json.loads(result)
            if parsed.get("status") == "error":
                return result

            message = parsed.get("message", "")
            if isinstance(message, str) and message.startswith("Opened profile screen"):
                for _ in range(20):
                    await asyncio.sleep(0.1)
                    state_text = await _get({"format": "json"})
                    state = json.loads(state_text)
                    if state.get("menu_screen") == "profile_select":
                        result = await _profiles_post(body)
                        parsed = json.loads(result)
                        if parsed.get("status") == "error":
                            return result
                        break
            result = await _wait_for_profile(profile_id, result)
        except json.JSONDecodeError:
            pass
        return result
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def delete_profile(profile_id: int) -> str:
    """Delete an inactive profile slot.

    The active profile cannot be deleted through this tool. Switch away first if
    you intend to remove a slot after backing up any data you need.

    Args:
        profile_id: Profile slot to delete. Must be 1, 2, or 3.
    """
    try:
        return await _profiles_post({"action": "delete", "profile_id": profile_id})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def use_potion(slot: int, target: str | None = None) -> str:
    """Use a potion from the player's potion slots.

    Works both during and outside of combat. Combat-only potions require an active battle.

    Args:
        slot: Potion slot index (as shown in game state).
        target: Entity ID of the target enemy (e.g. "JAW_WORM_0"). Required for enemy-targeted potions.
    """
    body: dict = {"action": "use_potion", "slot": slot}
    if target is not None:
        body["target"] = target
    try:
        return await _post(body)
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def discard_potion(slot: int) -> str:
    """Discard a potion from the player's potion slots to free up space.

    Use this when all potion slots are full and you need room for incoming potions
    (e.g. before collecting a potion reward).

    Args:
        slot: Potion slot index to discard (as shown in game state).
    """
    try:
        return await _post({"action": "discard_potion", "slot": slot})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def proceed_to_map() -> str:
    """Proceed from the current screen to the map.

    Works from: rewards screen, rest site, shop, fake merchant.
    Does NOT work for events — use event_choose_option() with the Proceed option's index.
    """
    try:
        return await _post({"action": "proceed"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Combat (state_type: monster / elite / boss)
# ---------------------------------------------------------------------------


@mcp.tool()
async def combat_play_card(card_index: int, target: str | None = None) -> str:
    """[Combat] Play a card from the player's hand.

    Args:
        card_index: Index of the card in hand (0-based, as shown in game state).
        target: Entity ID of the target enemy (e.g. "JAW_WORM_0"). Required for single-target cards.

    Note that the index can change as cards are played - playing a card will shift the indices of remaining cards in hand.
    Refer to the latest game state for accurate indices. New cards are drawn to the right, so playing cards from right to left can help maintain more stable indices for remaining cards.
    """
    body: dict = {"action": "play_card", "card_index": card_index}
    if target is not None:
        body["target"] = target
    try:
        return await _post(body)
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def combat_end_turn() -> str:
    """[Combat] End the player's current turn."""
    try:
        return await _post({"action": "end_turn"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# In-Combat Card Selection (state_type: hand_select)
# ---------------------------------------------------------------------------


@mcp.tool()
async def combat_select_card(card_index: int) -> str:
    """[Combat Selection] Select a card from hand during an in-combat card selection prompt.

    Used when a card effect asks you to select a card to exhaust, discard, etc.
    This is different from deck_select_card which handles out-of-combat card selection overlays.

    Args:
        card_index: 0-based index of the card in the selectable hand cards (as shown in game state).
    """
    try:
        return await _post({"action": "combat_select_card", "card_index": card_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def combat_confirm_selection() -> str:
    """[Combat Selection] Confirm the in-combat card selection.

    After selecting the required number of cards from hand (exhaust, discard, etc.),
    use this to confirm the selection. Only works when the confirm button is enabled.
    """
    try:
        return await _post({"action": "combat_confirm_selection"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Rewards (state_type: rewards / card_reward)
# ---------------------------------------------------------------------------


@mcp.tool()
async def rewards_claim(reward_index: int) -> str:
    """[Rewards] Claim a reward from the post-combat rewards screen.

    Gold, potion, and relic rewards are claimed immediately.
    Card rewards open the card selection screen (state changes to card_reward).

    Args:
        reward_index: 0-based index of the reward on the rewards screen.

    Note that claiming a reward may change the indices of remaining rewards, so refer to the latest game state for accurate indices.
    Claiming from right to left can help maintain more stable indices for remaining rewards, as rewards will always shift left to fill in gaps.
    """
    try:
        return await _post({"action": "claim_reward", "index": reward_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def rewards_pick_card(card_index: int) -> str:
    """[Rewards] Select a card from the card reward selection screen.

    Args:
        card_index: 0-based index of the card to add to the deck.
    """
    try:
        return await _post({"action": "select_card_reward", "card_index": card_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def rewards_skip_card() -> str:
    """[Rewards] Skip the card reward without selecting a card."""
    try:
        return await _post({"action": "skip_card_reward"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Map (state_type: map)
# ---------------------------------------------------------------------------


@mcp.tool()
async def map_choose_node(node_index: int) -> str:
    """[Map] Choose a map node to travel to.

    Args:
        node_index: 0-based index of the node from the next_options list.
    """
    try:
        return await _post({"action": "choose_map_node", "index": node_index})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Rest Site (state_type: rest_site)
# ---------------------------------------------------------------------------


@mcp.tool()
async def rest_choose_option(option_index: int) -> str:
    """[Rest Site] Choose a rest site option (rest, smith, etc.).

    Args:
        option_index: 0-based index of the option from the rest site state.
    """
    try:
        return await _post({"action": "choose_rest_option", "index": option_index})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Shop (state_type: shop)
# ---------------------------------------------------------------------------


@mcp.tool()
async def shop_purchase(item_index: int) -> str:
    """[Shop / Fake Merchant] Purchase an item from the shop.

    Works for both regular shops (state_type: shop) and the fake merchant
    event (state_type: fake_merchant). The fake merchant only sells relics.

    Args:
        item_index: 0-based index of the item from the shop state.
    """
    try:
        return await _post({"action": "shop_purchase", "index": item_index})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Event (state_type: event)
# ---------------------------------------------------------------------------


@mcp.tool()
async def event_choose_option(option_index: int) -> str:
    """[Event] Choose an event option.

    Works for both regular events and ancients (after dialogue ends).
    Also used to click the Proceed option after an event resolves.

    Args:
        option_index: 0-based index of the option from the event state.
    """
    try:
        return await _post({"action": "choose_event_option", "index": option_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def event_advance_dialogue() -> str:
    """[Event] Advance ancient event dialogue.

    Click through dialogue text in ancient events. Call repeatedly until options appear.
    """
    try:
        return await _post({"action": "advance_dialogue"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Card Selection (state_type: card_select)
# ---------------------------------------------------------------------------


@mcp.tool()
async def deck_select_card(card_index: int) -> str:
    """[Card Selection] Select or deselect a card in the card selection screen.

    Used when the game asks you to choose cards from your deck (transform, upgrade,
    remove, discard) or pick a card from offered choices (potions, effects).

    For deck selections: toggles card selection. For choose-a-card: picks immediately.

    Args:
        card_index: 0-based index of the card (as shown in game state).
    """
    try:
        return await _post({"action": "select_card", "index": card_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def deck_confirm_selection() -> str:
    """[Card Selection] Confirm the current card selection.

    After selecting the required number of cards, use this to confirm.
    If a preview is showing (e.g., transform preview), this confirms the preview.
    Not needed for choose-a-card screens where picking is immediate.
    """
    try:
        return await _post({"action": "confirm_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def deck_cancel_selection() -> str:
    """[Card Selection] Cancel the current card selection.

    If a preview is showing, goes back to the selection grid.
    For choose-a-card screens, clicks the skip button (if available).
    Otherwise, closes the card selection screen (only if cancellation is allowed).
    """
    try:
        return await _post({"action": "cancel_selection"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Bundle Selection (state_type: bundle_select)
# ---------------------------------------------------------------------------


@mcp.tool()
async def bundle_select(bundle_index: int) -> str:
    """[Bundle Selection] Open a bundle preview.

    Args:
        bundle_index: 0-based index of the bundle.
    """
    try:
        return await _post({"action": "select_bundle", "index": bundle_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def bundle_confirm_selection() -> str:
    """[Bundle Selection] Confirm the currently previewed bundle."""
    try:
        return await _post({"action": "confirm_bundle_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def bundle_cancel_selection() -> str:
    """[Bundle Selection] Cancel the current bundle preview."""
    try:
        return await _post({"action": "cancel_bundle_selection"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Relic Selection (state_type: relic_select)
# ---------------------------------------------------------------------------


@mcp.tool()
async def relic_select(relic_index: int) -> str:
    """[Relic Selection] Select a relic from the relic selection screen.

    Used when the game offers a choice of relics (e.g., boss relic rewards).

    Args:
        relic_index: 0-based index of the relic (as shown in game state).
    """
    try:
        return await _post({"action": "select_relic", "index": relic_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def relic_skip() -> str:
    """[Relic Selection] Skip the relic selection without choosing a relic."""
    try:
        return await _post({"action": "skip_relic_selection"})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Treasure (state_type: treasure)
# ---------------------------------------------------------------------------


@mcp.tool()
async def treasure_claim_relic(relic_index: int) -> str:
    """[Treasure] Claim a relic from the treasure chest.

    The chest is auto-opened when entering the treasure room.
    After claiming, use proceed_to_map() to continue.

    Args:
        relic_index: 0-based index of the relic (as shown in game state).
    """
    try:
        return await _post({"action": "claim_treasure_relic", "index": relic_index})
    except Exception as e:
        return _handle_error(e)


# ---------------------------------------------------------------------------
# Crystal Sphere (state_type: crystal_sphere)
# ---------------------------------------------------------------------------


@mcp.tool()
async def crystal_sphere_set_tool(tool: str) -> str:
    """[Crystal Sphere] Switch the active divination tool.

    Args:
        tool: Either "big" or "small".
    """
    try:
        return await _post({"action": "crystal_sphere_set_tool", "tool": tool})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def crystal_sphere_click_cell(x: int, y: int) -> str:
    """[Crystal Sphere] Click a hidden cell on the Crystal Sphere grid.

    Args:
        x: Cell x-coordinate.
        y: Cell y-coordinate.
    """
    try:
        return await _post({"action": "crystal_sphere_click_cell", "x": x, "y": y})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def crystal_sphere_proceed() -> str:
    """[Crystal Sphere] Continue after the Crystal Sphere minigame finishes."""
    try:
        return await _post({"action": "crystal_sphere_proceed"})
    except Exception as e:
        return _handle_error(e)


# ===========================================================================
# MULTIPLAYER tools — all route through /api/v1/multiplayer
# ===========================================================================


@mcp.tool()
async def mp_get_game_state(format: str = "markdown") -> str:
    """[Multiplayer] Get the current multiplayer game state.

    Returns a summary of all players (HP, gold, alive status) plus full
    detail for the local player (relics, potions, deck, etc.), along with
    multiplayer-specific data: map votes, event votes, treasure bids,
    end-turn ready status. Only works during a multiplayer run.

    Args:
        format: "markdown" for human-readable output, "json" for structured data.
    """
    try:
        return await _mp_get({"format": format})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_combat_play_card(card_index: int, target: str | None = None) -> str:
    """[Multiplayer Combat] Play a card from the local player's hand.

    Same as singleplayer combat_play_card but routed through the multiplayer
    endpoint for sync safety.

    Args:
        card_index: Index of the card in hand (0-based).
        target: Entity ID of the target enemy (e.g. "JAW_WORM_0"). Required for single-target cards.
    """
    body: dict = {"action": "play_card", "card_index": card_index}
    if target is not None:
        body["target"] = target
    try:
        return await _mp_post(body)
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_combat_end_turn() -> str:
    """[Multiplayer Combat] Submit end-turn vote.

    In multiplayer, ending the turn is a VOTE — the turn only ends when ALL
    players have submitted. Use mp_combat_undo_end_turn() to retract.
    """
    try:
        return await _mp_post({"action": "end_turn"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_combat_undo_end_turn() -> str:
    """[Multiplayer Combat] Retract end-turn vote.

    If you submitted end turn but want to play more cards, use this to undo.
    Only works if other players haven't all committed yet.
    """
    try:
        return await _mp_post({"action": "undo_end_turn"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_use_potion(slot: int, target: str | None = None) -> str:
    """[Multiplayer] Use a potion from the local player's potion slots.

    Args:
        slot: Potion slot index (as shown in game state).
        target: Entity ID of the target enemy. Required for enemy-targeted potions.
    """
    body: dict = {"action": "use_potion", "slot": slot}
    if target is not None:
        body["target"] = target
    try:
        return await _mp_post(body)
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_discard_potion(slot: int) -> str:
    """[Multiplayer] Discard a potion from the local player's potion slots to free up space.

    Args:
        slot: Potion slot index to discard (as shown in game state).
    """
    try:
        return await _mp_post({"action": "discard_potion", "slot": slot})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_map_vote(node_index: int) -> str:
    """[Multiplayer Map] Vote for a map node to travel to.

    In multiplayer, map selection is a vote — travel happens when all players
    agree. Re-voting for the same node sends a ping to other players.

    Args:
        node_index: 0-based index of the node from the next_options list.
    """
    try:
        return await _mp_post({"action": "choose_map_node", "index": node_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_event_choose_option(option_index: int) -> str:
    """[Multiplayer Event] Choose or vote for an event option.

    For shared events: this is a vote (resolves when all players vote).
    For individual events: immediate choice, same as singleplayer.

    Args:
        option_index: 0-based index of the option from the event state.
    """
    try:
        return await _mp_post({"action": "choose_event_option", "index": option_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_event_advance_dialogue() -> str:
    """[Multiplayer Event] Advance ancient event dialogue."""
    try:
        return await _mp_post({"action": "advance_dialogue"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_rest_choose_option(option_index: int) -> str:
    """[Multiplayer Rest Site] Choose a rest site option (rest, smith, etc.).

    Per-player choice — no voting needed.

    Args:
        option_index: 0-based index of the option.
    """
    try:
        return await _mp_post({"action": "choose_rest_option", "index": option_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_shop_purchase(item_index: int) -> str:
    """[Multiplayer Shop] Purchase an item from the shop.

    Per-player inventory — no voting needed.

    Args:
        item_index: 0-based index of the item.
    """
    try:
        return await _mp_post({"action": "shop_purchase", "index": item_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_rewards_claim(reward_index: int) -> str:
    """[Multiplayer Rewards] Claim a reward from the post-combat rewards screen.

    Args:
        reward_index: 0-based index of the reward.
    """
    try:
        return await _mp_post({"action": "claim_reward", "index": reward_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_rewards_pick_card(card_index: int) -> str:
    """[Multiplayer Rewards] Select a card from the card reward screen.

    Args:
        card_index: 0-based index of the card to add to the deck.
    """
    try:
        return await _mp_post({"action": "select_card_reward", "card_index": card_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_rewards_skip_card() -> str:
    """[Multiplayer Rewards] Skip the card reward."""
    try:
        return await _mp_post({"action": "skip_card_reward"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_proceed_to_map() -> str:
    """[Multiplayer] Proceed from the current screen to the map.

    Works from: rewards screen, rest site, shop.
    """
    try:
        return await _mp_post({"action": "proceed"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_deck_select_card(card_index: int) -> str:
    """[Multiplayer Card Selection] Select or deselect a card in the card selection screen.

    Args:
        card_index: 0-based index of the card.
    """
    try:
        return await _mp_post({"action": "select_card", "index": card_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_deck_confirm_selection() -> str:
    """[Multiplayer Card Selection] Confirm the current card selection."""
    try:
        return await _mp_post({"action": "confirm_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_deck_cancel_selection() -> str:
    """[Multiplayer Card Selection] Cancel the current card selection."""
    try:
        return await _mp_post({"action": "cancel_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_bundle_select(bundle_index: int) -> str:
    """[Multiplayer Bundle Selection] Open a bundle preview.

    Args:
        bundle_index: 0-based index of the bundle.
    """
    try:
        return await _mp_post({"action": "select_bundle", "index": bundle_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_bundle_confirm_selection() -> str:
    """[Multiplayer Bundle Selection] Confirm the currently previewed bundle."""
    try:
        return await _mp_post({"action": "confirm_bundle_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_bundle_cancel_selection() -> str:
    """[Multiplayer Bundle Selection] Cancel the current bundle preview."""
    try:
        return await _mp_post({"action": "cancel_bundle_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_combat_select_card(card_index: int) -> str:
    """[Multiplayer Combat Selection] Select a card from hand during in-combat card selection.

    Args:
        card_index: 0-based index of the card in the selectable hand cards.
    """
    try:
        return await _mp_post({"action": "combat_select_card", "card_index": card_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_combat_confirm_selection() -> str:
    """[Multiplayer Combat Selection] Confirm the in-combat card selection."""
    try:
        return await _mp_post({"action": "combat_confirm_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_relic_select(relic_index: int) -> str:
    """[Multiplayer Relic Selection] Select a relic (boss relic rewards).

    Args:
        relic_index: 0-based index of the relic.
    """
    try:
        return await _mp_post({"action": "select_relic", "index": relic_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_relic_skip() -> str:
    """[Multiplayer Relic Selection] Skip the relic selection."""
    try:
        return await _mp_post({"action": "skip_relic_selection"})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_treasure_claim_relic(relic_index: int) -> str:
    """[Multiplayer Treasure] Bid on / claim a relic from the treasure chest.

    In multiplayer, this is a bid — if multiple players pick the same relic,
    a "relic fight" determines the winner. Others get consolation prizes.

    Args:
        relic_index: 0-based index of the relic.
    """
    try:
        return await _mp_post({"action": "claim_treasure_relic", "index": relic_index})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_crystal_sphere_set_tool(tool: str) -> str:
    """[Multiplayer Crystal Sphere] Switch the active divination tool.

    Args:
        tool: Either "big" or "small".
    """
    try:
        return await _mp_post({"action": "crystal_sphere_set_tool", "tool": tool})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_crystal_sphere_click_cell(x: int, y: int) -> str:
    """[Multiplayer Crystal Sphere] Click a hidden cell on the Crystal Sphere grid.

    Args:
        x: Cell x-coordinate.
        y: Cell y-coordinate.
    """
    try:
        return await _mp_post({"action": "crystal_sphere_click_cell", "x": x, "y": y})
    except Exception as e:
        return _handle_error(e)


@mcp.tool()
async def mp_crystal_sphere_proceed() -> str:
    """[Multiplayer Crystal Sphere] Continue after the Crystal Sphere minigame finishes."""
    try:
        return await _mp_post({"action": "crystal_sphere_proceed"})
    except Exception as e:
        return _handle_error(e)


def main():
    parser = argparse.ArgumentParser(description="STS2 MCP Server")
    parser.add_argument("--port", type=int, default=15526, help="Game HTTP server port")
    parser.add_argument("--host", type=str, default="localhost", help="Game HTTP server host")
    parser.add_argument("--no-trust-env", action="store_true", help="Ignore HTTP_PROXY/HTTPS_PROXY environment variables")
    args = parser.parse_args()

    global _base_url, _trust_env
    _base_url = f"http://{args.host}:{args.port}"
    _trust_env = not args.no_trust_env

    _print_log_startup_message()
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
