import pytest

from bot.db import add_message, clear_messages, init_db, recent_messages, trim_messages


@pytest.mark.asyncio
async def test_user_memory_isolated_and_reset(tmp_path):
    db = tmp_path / "memory.db"
    await init_db(db)
    for i in range(7):
        await add_message(db, 1, "user", f"сообщение {i}")
    await add_message(db, 2, "user", "чужое сообщение")
    await trim_messages(db, 1, 4)
    own = await recent_messages(db, 1, 100)
    other = await recent_messages(db, 2, 100)
    assert len(own) == 4
    assert own[0]["content"] == "сообщение 3"
    assert other == [{"role": "user", "content": "чужое сообщение"}]
    await clear_messages(db, 1)
    assert await recent_messages(db, 1, 100) == []
    assert await recent_messages(db, 2, 100) == other
