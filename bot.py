import asyncio
import os
import logging
from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher
from handlers import commands, media
from middlewares.access import AccessMiddleware

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

dp.message.middleware(AccessMiddleware())

dp.include_router(commands.router)
dp.include_router(media.router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())