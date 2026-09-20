from __future__ import annotations

from pathlib import Path

import aiosqlite


async def init_db(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    async with aiosqlite.connect(path) as db:
        await db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            username TEXT,
            full_name TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """)
        await db.commit()


async def upsert_user(path: Path, telegram_id: int, username: str | None, full_name: str) -> None:
    async with aiosqlite.connect(path) as db:
        await db.execute("""
            INSERT INTO users (telegram_id, username, full_name) VALUES (?, ?, ?)
            ON CONFLICT(telegram_id) DO UPDATE SET username=excluded.username, full_name=excluded.full_name
        """, (telegram_id, username, full_name))
        await db.commit()


async def add_message(path: Path, telegram_id: int, role: str, content: str) -> None:
    async with aiosqlite.connect(path) as db:
        await db.execute("INSERT INTO messages (telegram_id, role, content) VALUES (?, ?, ?)", (telegram_id, role, content))
        await db.commit()


async def recent_messages(path: Path, telegram_id: int, limit: int) -> list[dict[str, str]]:
    async with aiosqlite.connect(path) as db:
        cursor = await db.execute(
            "SELECT role, content FROM messages WHERE telegram_id=? ORDER BY id DESC LIMIT ?",
            (telegram_id, limit),
        )
        rows = await cursor.fetchall()
    return [{"role": role, "content": content} for role, content in reversed(rows)]


async def clear_messages(path: Path, telegram_id: int) -> None:
    async with aiosqlite.connect(path) as db:
        await db.execute("DELETE FROM messages WHERE telegram_id=?", (telegram_id,))
        await db.commit()
