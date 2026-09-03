import os
import logging
from aiogram import BaseMiddleware
from aiogram.types import Message

ALLOWED_USER_ID = int(os.getenv("ALLOWED_USER_ID"))


class AccessMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        username = event.from_user.username

        if user_id != ALLOWED_USER_ID:
            logging.warning(f"Unauthorized access attempt: user_id={user_id}, username={username}")
            return

        content_type = event.content_type
        logging.info(f"Message from user_id={user_id}, username={username}, type={content_type}")

        return await handler(event, data)