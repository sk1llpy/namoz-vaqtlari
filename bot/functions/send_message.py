import datetime
from aiogram import types

from loader import bot
from keyboards.inline.notification import notification_btn


async def send_message_prayer_on_time(user: dict, prayer: str):
    if user['notification']:
        try:
            await bot.send_message(chat_id=int(user['id']), text=f"<b>{prayer} namozi vaqti bo'ldi ⏰</b>\n\n<i>📍 Shahar (viloyat): {user['region']}\n✏️ Shaharni o'zgartirish uchun Sozlamalar qismiga kiring ⚙️</i>",
                reply_markup=notification_btn)
        except Exception as exc:
            print(f"handlers/send_notification.py #ERROR     [{datetime.datetime.now()}]  {exc}")