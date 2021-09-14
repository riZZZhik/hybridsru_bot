from aiogram import Dispatcher, types

from .handlers import save_image


def setup_bot(dp: Dispatcher):
    """Setup message handlers."""
    dp.register_message_handler(save_image, content_types=types.ContentType.PHOTO)
    return ", ".join(["save_image"])


__all__ = ["setup_bot"]
