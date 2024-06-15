from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import CommandHelp


@dp.message_handler(CommandHelp(), lambda message: not str(message.chat.id).startswith("-"))
async def help_handler(message: types.Message):
    await message.answer(
        text = f"""<b>Ushbu bot yordamida siz namoz vaqtlarini ko'rishingiz, haftalik taqvimni ko'rishingiz, tasbihdan foydalanishingiz mumkin. Va Bot xar namoz vaqtida sizni ogoxlantirib turadi 😊</b>
        
<i>ℹ️ Manba: islom.uz
🧑‍💻 Yaratuvchi: @unrsk1ll</i>"""
    )