from __future__ import annotations

import httpx

from bot.config import Settings


class AIService:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings

    async def answer(self, history: list[dict[str, str]]) -> str:
        if not self.settings.ai_base_url or not self.settings.ai_model:
            raise RuntimeError("AI_BASE_URL или AI_MODEL не заданы")
        payload = {
            "model": self.settings.ai_model,
            "messages": [{"role": "system", "content": self.settings.system_prompt}, *history],
        }
        headers = {"Authorization": f"Bearer {self.settings.ai_api_key}"}
        async with httpx.AsyncClient(timeout=90) as client:
            response = await client.post(
                f"{self.settings.ai_base_url}/chat/completions",
                json=payload,
                headers=headers,
            )
            response.raise_for_status()
            data = response.json()
        return str(data["choices"][0]["message"]["content"]).strip()
