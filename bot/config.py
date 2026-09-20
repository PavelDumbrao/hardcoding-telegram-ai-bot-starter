from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    bot_token: str
    admin_ids: frozenset[int]
    db_path: Path
    log_level: str
    ai_base_url: str
    ai_api_key: str
    ai_model: str
    ai_history_limit: int
    system_prompt: str


def _parse_admin_ids(raw: str) -> frozenset[int]:
    return frozenset(int(x.strip()) for x in raw.split(",") if x.strip())


def load_settings() -> Settings:
    load_dotenv()
    bot_token = os.getenv("BOT_TOKEN", "").strip()
    ai_api_key = os.getenv("AI_API_KEY", "").strip()
    if not bot_token:
        raise RuntimeError("BOT_TOKEN не задан. Добавь его локально в .env")
    if not ai_api_key:
        raise RuntimeError("AI_API_KEY не задан. Добавь его локально в .env")
    return Settings(
        bot_token=bot_token,
        admin_ids=_parse_admin_ids(os.getenv("ADMIN_IDS", "")),
        db_path=Path(os.getenv("DB_PATH", "data/bot.sqlite3")),
        log_level=os.getenv("LOG_LEVEL", "INFO").upper(),
        ai_base_url=os.getenv("AI_BASE_URL", "").rstrip("/"),
        ai_api_key=ai_api_key,
        ai_model=os.getenv("AI_MODEL", "").strip(),
        ai_history_limit=max(2, int(os.getenv("AI_HISTORY_LIMIT", "12"))),
        system_prompt=os.getenv("SYSTEM_PROMPT", "Ты полезный ассистент. Отвечай кратко и по делу."),
    )
