from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("⬅️ Orqaga", callback_data='backto_prayer_time')
    ]
])

back_btn_week = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("⬅️ Orqaga", callback_data='backtoweek_prayer_time')
    ]
])