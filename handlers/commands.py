from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой личный ассистент.")


@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("Доступные команды:\n/start\n/help\n/reminders")


@router.message(Command("reminders"))
async def cmd_reminders(message: types.Message):
    await message.answer("У тебя пока нет напоминаний.")