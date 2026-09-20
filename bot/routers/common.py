import logging

from aiogram import F, Router
from aiogram.enums import ChatAction
from aiogram.types import Message

from bot.config import Settings
from bot.db import add_message, recent_messages
from bot.services.ai import AIService
from bot.services.text import split_text

router = Router(name="common")
logger = logging.getLogger(__name__)


@router.message(F.text == "Что умеет бот")
async def about_handler(message: Message) -> None:
    await message.answer("Я отвечаю через подключённую ИИ-модель. Codex / Claude Code может адаптировать мою роль под твой проект.")


@router.message(F.text == "Помощь")
async def menu_help_handler(message: Message) -> None:
    await message.answer("Напиши вопрос. Для очистки памяти используй /reset.")


@router.message(F.text)
async def ai_handler(message: Message, settings: Settings) -> None:
    if not message.from_user or not message.text:
        return
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    await add_message(settings.db_path, message.from_user.id, "user", message.text)
    history = await recent_messages(settings.db_path, message.from_user.id, settings.ai_history_limit)
    try:
        answer = await AIService(settings).answer(history)
    except Exception:
        logger.exception("Ошибка ИИ-провайдера")
        await message.answer("Не получилось получить ответ от ИИ. Попробуй ещё раз чуть позже.")
        return
    await add_message(settings.db_path, message.from_user.id, "assistant", answer)
    for part in split_text(answer):
        await message.answer(part)
