from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def user_btn(name: str, username: str = None):
    if username:
        button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(name, url=f'https://t.me/{username}')
                ]
            ]
        )
    else:
        button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(name, callback_data=f'user_is_private')
                ]
            ]
        )
    
    return button