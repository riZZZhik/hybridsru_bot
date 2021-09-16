import os
from uuid import uuid4

from aiogram import types
from loguru import logger


async def save_image(message: types.Message):
    # Get current time
    dt = message.date

    # Get path to save directory
    save_dir = os.path.join(message.bot.get("save_dir"), dt.strftime("%Y"), dt.strftime("%B"), dt.strftime("%d"))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save image
    save_path = os.path.join(save_dir, dt.strftime(f"%H часов %M минут ({str(uuid4())}).jpg"))
    await message.photo[-1].download(save_path)

    # Log event
    logger.info('Saved image from "%s" chat to "%s" file' % (message.chat.title, save_path))
