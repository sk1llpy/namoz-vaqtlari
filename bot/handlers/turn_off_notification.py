from loader import dp ,bot
from aiogram import types

from functions.API.users.update_user import update_user_notification
from functions.API.users import get_user


@dp.callback_query_handler(text=['turn_off_notification'])
async def turn_off_notification(call: types.CallbackQuery):
    user_id = call.from_user.id
    user = get_user(user_id=user_id)

    if user.status_code == 200:
        if user.json()['notification'] if user.json()['notification'] else False:
            try:
                response = update_user_notification(
                    user_id = user_id,
                    notification = False
                )
            except Exception as exc: print(f"[ERROR_TELEGRAM_BOT] Update User (notification): {exc}")

            if response.status_code == 200:
                try:
                    await bot.delete_message(
                        chat_id = call.message.chat.id,
                        message_id = call.message.message_id
                    )
                    await bot.send_message(
                        chat_id = call.message.chat.id,
                        text = f"""<b>Bildirishnoma o'chirildi 🔕</b>

        <i>Bildirishnomani yoqish uchun "Sozlamar" qismiga kiring ⚙️</i>""",
                    )
                except Exception as exc: print(f"[ERROR_TELEGRAM_BOT] Send message: {exc}")
            else:
                try:
                    await call.message.answer(
                        text = f"""<b>Xatolik yuz berdi ❌</b>"""
                    )
                except Exception as exc: print(f"[ERROR_TELEGRAM_BOT] Send message: {exc}")
