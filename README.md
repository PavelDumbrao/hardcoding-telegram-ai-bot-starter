# 🤖 Hardcoding PRO — Telegram AI Bot Starter

**Один шаблон → свой Telegram AI-бот → база для будущего AI-агента.**

[📘 Урок с проверками](LESSON_01.md) · [🧩 Промпт для Codex / Claude Code / ZCode](PROMPT_ADAPT.md) · [🗺 Архитектура](ARCHITECTURE.md) · [🔎 Исследование 145 GitHub-репозиториев](RESEARCH_100_SOURCES.md)

## Что готово

- `/start`, `/help`, `/reset` и кнопки меню;
- ответы ИИ через OpenAI-compatible `/chat/completions`;
- ограниченная память в SQLite, отдельная для каждого пользователя;
- только личные чаты — без сбора сообщений групп;
- локальный `.env`, события аналитики, тесты и GitHub Actions.

**Это учебный AI-ассистент**, не автономный агент с инструментами. Tool calling, RAG и CRM добавим после успешного первого запуска.

## 🚀 Быстрый запуск

### 1. Создай копию

Нажми **Use this template → Create a new repository** на GitHub. Новый проект должен принадлежать тебе. Открой его в Codex / Claude Code / ZCode или клонируй на компьютер.

### 2. Подготовь Python 3.12

Mac/Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
cp .env.example .env
```

Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -e ".[dev]"
Copy-Item .env.example .env
```

### 3. Внеси токены только в локальный `.env`

Создай Telegram-бота в [@BotFather](https://t.me/BotFather) командой `/newbot`. Заполни `BOT_TOKEN`, `AI_API_KEY` и `AI_MODEL`. В `.env.example` указан пример URL для OpenAI; если у тебя другой провайдер, замени `AI_BASE_URL` на его Chat Completions base URL (обычно заканчивается `/v1`).

```dotenv
BOT_TOKEN=ТОКЕН_ИЗ_BOTFATHER
AI_BASE_URL=https://api.openai.com/v1
AI_API_KEY=КЛЮЧ_ТВОЕГО_ПРОВАЙДЕРА
AI_MODEL=МОДЕЛЬ_ДОСТУПНАЯ_У_ТВОЕГО_ПРОВАЙДЕРА
```

Сам Telegram Bot API доступен бесплатно, но вызовы ИИ могут тарифицироваться отдельно и требуют доступа к API. **Не отправляй секреты в чаты, коммиты, PR или скриншоты.**

### 4. Запусти бота

Mac/Linux: `python -m bot.main` (в активированном окружении).

Windows: `.venv\Scripts\python.exe -m bot.main`.

Открой своего бота в Telegram и проверь `/start` → текстовый вопрос → уточнение → `/reset`. Терминал должен оставаться работающим. Для локального запуска не нужны сервер, домен, Docker или webhook. **Один BOT_TOKEN — один polling-процесс.**

## ✅ Офлайн-проверки без токенов

```bash
pytest -q
ruff check .
python -m compileall -q bot
```

Офлайн-тесты **не доказывают**, что работают внешние Telegram/AI API. Живой E2E проверяется отдельно с личными токенами ученика.

## Частые проблемы

| Симптом | Что проверить |
|---|---|
| `BOT_TOKEN не задан` | Локальный файл `.env` и токен BotFather |
| `AI_API_KEY/AI_BASE_URL/AI_MODEL не задан` | Все обязательные настройки ИИ |
| `401 Unauthorized` | Правильность ключа и доступ к API |
| `404 model not found` | ID модели и base URL именно твоего провайдера |
| `Conflict: terminated by other getUpdates request` | Не запущен ли второй экземпляр этого бота |
| Команды работают, ИИ нет | Настройки AI, сеть, баланс/лимиты и лог ошибок |
| После закрытия ноутбука бот молчит | Для 24/7 потребуется хостинг |

## С чего продолжить

Начни с [LESSON_01.md](LESSON_01.md): **задание → действие → проверка → следующий блок**. Затем скопируй [PROMPT_ADAPT.md](PROMPT_ADAPT.md) своему кодинг-агенту. MIT License.
