import json

import httpx
import pytest

from bot.config import Settings
from bot.services.ai import AIService


@pytest.mark.asyncio
async def test_openai_compatible_request(monkeypatch, tmp_path):
    settings = Settings(
        bot_token="TEST_TOKEN_NOT_REAL",
        admin_ids=frozenset(),
        db_path=tmp_path / "data.db",
        log_level="INFO",
        ai_base_url="https://example.test/v1",
        ai_api_key="TEST_KEY_NOT_REAL",
        ai_model="test-model",
        ai_history_limit=12,
        system_prompt="Ты ассистент",
    )

    def respond(request: httpx.Request) -> httpx.Response:
        assert str(request.url) == "https://example.test/v1/chat/completions"
        assert request.headers["Authorization"] == "Bearer TEST_KEY_NOT_REAL"
        data = json.loads(request.content)
        assert data["model"] == "test-model"
        assert data["messages"] == [
            {"role": "system", "content": "Ты ассистент"},
            {"role": "user", "content": "Привет"},
        ]
        return httpx.Response(200, json={"choices": [{"message": {"content": "  Привет!  "}}]})

    transport = httpx.MockTransport(respond)
    real_client = httpx.AsyncClient
    monkeypatch.setattr(
        httpx, "AsyncClient", lambda **kwargs: real_client(transport=transport, **kwargs)
    )
    assert await AIService(settings).answer([{"role": "user", "content": "Привет"}]) == "Привет!"
