from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart

from loader import dp, bot
from functions.API.users.create_user import create_user
from keyboards.reply.menu import menu_btn
from text import text


@dp.message_handler(CommandStart())
async def send_welcome(message: types.Message):
    create_user(message.from_user.id)

    await message.answer(
        text = text.START(
            name = message.from_user.first_name
        ),
        reply_markup = menu_btn(message.from_user.id)
    )