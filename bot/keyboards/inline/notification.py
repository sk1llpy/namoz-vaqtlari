from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

notification_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🔕 Bildirishnomani o'chirish", callback_data='turn_off_notification')
    ]
])