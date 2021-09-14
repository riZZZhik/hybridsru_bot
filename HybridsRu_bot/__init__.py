from aiogram import Dispatcher, types

from .handlers import echo, save_image


def setup_bot(dp: Dispatcher):
    """Setup message handlers."""
    dp.register_message_handler(save_image, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(echo)
    return ", ".join(["save_image", "echo"])


__all__ = ["setup_bot"]
