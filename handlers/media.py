import os
import uuid
import logging
from aiogram import Router, types, Bot

router = Router()

os.makedirs("downloads", exist_ok=True)


@router.message(lambda message: message.voice is not None)
async def handle_voice(message: types.Message, bot: Bot):
    try:
        file = await bot.get_file(message.voice.file_id)
        filename = f"downloads/voice_{uuid.uuid4().hex}.ogg"
        await bot.download_file(file.file_path, filename)
        await message.answer("Голосовое сообщение получено!")
    except Exception as e:
        logging.error(f"Error handling voice: {e}")
        await message.answer("Произошла ошибка при обработке голосового сообщения.")


@router.message(lambda message: message.photo is not None)
async def handle_photo(message: types.Message, bot: Bot):
    try:
        file = await bot.get_file(message.photo[-1].file_id)
        filename = f"downloads/photo_{uuid.uuid4().hex}.jpg"
        await bot.download_file(file.file_path, filename)
        await message.answer("Фото получено!")
    except Exception as e:
        logging.error(f"Error handling photo: {e}")
        await message.answer("Произошла ошибка при обработке фото.")


@router.message(lambda message: message.video is not None)
async def handle_video(message: types.Message, bot: Bot):
    try:
        file = await bot.get_file(message.video.file_id)
        filename = f"downloads/video_{uuid.uuid4().hex}.mp4"
        await bot.download_file(file.file_path, filename)
        await message.answer("Видео получено!")
    except Exception as e:
        logging.error(f"Error handling video: {e}")
        await message.answer("Произошла ошибка при обработке видео.")


@router.message(lambda message: message.text is not None)
async def echo(message: types.Message):
    try:
        await message.answer(f"Ты написал: {message.text}")
    except Exception as e:
        logging.error(f"Error handling text: {e}")
        await message.answer("Произошла ошибка при обработке сообщения.")


@router.message()
async def handle_unsupported(message: types.Message):
    await message.answer("Извини, я пока не умею обрабатывать этот тип сообщений.")