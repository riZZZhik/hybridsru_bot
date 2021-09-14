from aiogram import types


async def echo(message: types.Message):
    await message.answer(message.text)


async def save_image(message: types.Message):
    await message.answer("Это картинка, зуб даю")
