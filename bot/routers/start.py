from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from bot.config import Settings
from bot.db import clear_messages, upsert_user
from bot.keyboards import main_keyboard

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: Message, settings: Settings) -> None:
    if message.from_user:
        await upsert_user(settings.db_path, message.from_user.id, message.from_user.username, message.from_user.full_name)
    await message.answer("Привет! Я ИИ-бот. Опиши задачу обычным сообщением.", reply_markup=main_keyboard())


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer("Напиши вопрос. Команда /reset очищает память текущего диалога.")


@router.message(Command("reset"))
async def reset_handler(message: Message, settings: Settings) -> None:
    if message.from_user:
        await clear_messages(settings.db_path, message.from_user.id)
    await message.answer("Память диалога очищена.")
