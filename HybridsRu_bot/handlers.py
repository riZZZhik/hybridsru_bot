import os
from datetime import datetime

from aiogram import types
from loguru import logger


async def save_image(message: types.Message):
    # Get current time
    dt = datetime.now()

    # Get path to save directory
    save_dir = os.path.join(message.bot.get("save_dir"), dt.strftime("%Y"), dt.strftime("%B"), dt.strftime("%d"))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save image
    save_path = os.path.join(save_dir, dt.strftime("%H-%M-%S-%f.jpg"))
    await message.photo[-1].download(save_path)

    # Log event
    logger.info('Saved image from "%s" chat to "%s" file' % (message.chat.title, save_path))
