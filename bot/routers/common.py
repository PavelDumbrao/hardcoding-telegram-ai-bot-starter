import logging

from aiogram import F, Router
from aiogram.enums import ChatAction, ChatType
from aiogram.types import Message

from bot.analytics import track_event
from bot.config import Settings
from bot.db import add_message, recent_messages, trim_messages
from bot.services.ai import AIService
from bot.services.text import split_text

router = Router(name="common")
router.message.filter(F.chat.type == ChatType.PRIVATE)
logger = logging.getLogger(__name__)


@router.message(F.text == "Что умеет бот")
async def about_handler(message: Message, settings: Settings) -> None:
    await track_event(
        settings.db_path, message.from_user.id if message.from_user else None, "menu_about_clicked"
    )
    await message.answer(
        "Я отвечаю через ИИ и помню последние сообщения. Для очистки памяти — /reset."
    )


@router.message(F.text == "Помощь")
async def menu_help_handler(message: Message, settings: Settings) -> None:
    await track_event(
        settings.db_path, message.from_user.id if message.from_user else None, "menu_help_clicked"
    )
    await message.answer("Напиши вопрос. Команды: /start, /help, /reset.")


@router.message(F.text.startswith("/"))
async def unknown_command_handler(message: Message) -> None:
    await message.answer("Не знаю эту команду. Используй /start, /help или /reset.")


@router.message(F.text)
async def ai_handler(message: Message, settings: Settings) -> None:
    if not message.from_user or not message.text:
        return
    telegram_id = message.from_user.id
    await track_event(settings.db_path, telegram_id, "ai_request_started")
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    history = await recent_messages(settings.db_path, telegram_id, settings.ai_history_limit)
    history.append({"role": "user", "content": message.text})
    history = history[-settings.ai_history_limit :]
    try:
        answer = await AIService(settings).answer(history)
        if not answer:
            raise ValueError("Провайдер вернул пустой ответ")
    except Exception:
        logger.exception("Ошибка ИИ-провайдера")
        await track_event(settings.db_path, telegram_id, "ai_request_failed")
        await message.answer(
            "Не получилось получить ответ от ИИ. Проверь настройки или попробуй позже."
        )
        return
    # В историю попадают только успешные диалоги; хранение ограничено.
    await add_message(settings.db_path, telegram_id, "user", message.text)
    await add_message(settings.db_path, telegram_id, "assistant", answer)
    await trim_messages(settings.db_path, telegram_id, settings.ai_history_limit)
    await track_event(settings.db_path, telegram_id, "ai_request_succeeded")
    for part in split_text(answer):
        await message.answer(part)
