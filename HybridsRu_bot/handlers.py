import os
from datetime import datetime

from aiogram import types


async def save_image(message: types.Message):
    # Get current time
    time = datetime.now()

    # Get path to save directory
    save_dir = os.path.join(message.bot.get("save_dir"), time.strftime("%Y/%B/%d"))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Save image
    save_path = os.path.join(save_dir, time.strftime("%H:%M:%S.%f"))
    await message.photo[-1].download(save_path)
