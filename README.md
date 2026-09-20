# Hardcoding PRO: Telegram AI Bot Starter

Готовый шаблон Telegram-бота с подключением ИИ, памятью диалога и адаптацией через Codex / Claude Code.

## Что уже готово

- всё из базового Telegram Bot Starter
- подключение OpenAI-compatible API через `AI_BASE_URL`
- модель задаётся через `AI_MODEL`
- ограниченная память диалога в SQLite
- команда `/reset`
- безопасная обработка ошибок ИИ-провайдера
- готовый `PROMPT_ADAPT.md`

## Как использовать

1. Создай копию через **Use this template**.
2. Открой проект в Codex / Claude Code.
3. Вставь `PROMPT_ADAPT.md`.
4. Опиши роль и задачу бота.
5. Введи токены локально в `.env`, не в обычный чат.
6. Агент сам адаптирует, тестирует и запускает проект.

## Запуск

    cp .env.example .env
    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -e '.[dev]'
    python -m bot.main

## Проверки

    pytest -q
    ruff check .
    python -m compileall -q bot
