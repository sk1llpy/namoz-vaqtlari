from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from data.config import DOMAIN


def menu_btn(user_id):
    button = ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton("🧎 Namoz vaqtlari")
            ],
            [
                KeyboardButton("📿 Tasbih", web_app=WebAppInfo(url=f"{DOMAIN}?user_id={user_id}")),
                KeyboardButton("🤲 Zikr va duolar")
            ],
            [
                KeyboardButton("📅 Haftalik taqvim")
            ],
            [
                KeyboardButton("✍️ Izoh qoldirish"),
                KeyboardButton("⚙️ Sozlamalar")
            ]
        ]
    )
    
    return button