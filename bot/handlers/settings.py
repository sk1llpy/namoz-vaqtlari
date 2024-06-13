from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from functions.API.users import get_user
from states.settings import Settings as SettingsState
from keyboards.reply.settings import settings_btn


@dp.message_handler(text=["⚙️ Sozlamalar"])
async def settings_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = get_user(user_id=user_id)

    if user.status_code == 200:
        await SettingsState.command.set()
        await message.answer(
            text = f"""<b>Kerakli bo'limni tanlang 👇</b>""",
            reply_markup = settings_btn(notification = user.json()['notification'])
        )
    else:
        await message.answer("<b>Xatolik yuz berdi ❌</b>")


@dp.message_handler(text=["S"])