from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def settings_btn(notification: bool):
    if notification:
        button = ReplyKeyboardMarkup(
            keyboard = [
                [
                    KeyboardButton("📍 Shaharni o'zgartirish"),
                    KeyboardButton("🔕 Bildirishnomani o'chirish")
                ],
                [
                    KeyboardButton("⬅️ Orqaga")
                ]
            ],
            resize_keyboard = True,
            one_time_keyboard = True
        )
    else:
        button = ReplyKeyboardMarkup(
            keyboard = [
                [
                    KeyboardButton("📍 Shaharni o'zgartirish"),
                    KeyboardButton("🔔 Bildirishnomani yoqish")
                ],
                [
                    KeyboardButton("⬅️ Orqaga")
                ]
            ],
            resize_keyboard = True,
            one_time_keyboard = True
        )

    return button