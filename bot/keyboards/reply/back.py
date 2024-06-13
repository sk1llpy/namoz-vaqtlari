from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_btn = ReplyKeyboardMarkup(
    resize_keyboard = True,
    one_time_keyboard = True,
    keyboard = [
        [
            KeyboardButton("⬅️ Orqaga")
        ]
    ]
)