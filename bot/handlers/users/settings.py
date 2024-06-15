from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states.settings import Settings as SettingsState
from data.regions import REGIONS

from functions.API.users import get_user
from functions.API.users.update_user import update_user_region, update_user_notification

from keyboards.reply.settings import settings_btn
from keyboards.reply.menu import menu_btn
from keyboards.inline.regions import button_change as regions_btn
from keyboards.inline.back import back_btn


# Settings
@dp.message_handler(lambda message: not str(message.chat.id).startswith("-"), text=["⚙️ Sozlamalar"])
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


# Back to main menu
@dp.message_handler(lambda message: not str(message.chat.id).startswith("-"), text=["⬅️ Orqaga"], state=SettingsState.command)
async def settings_handler(message: types.Message, state: FSMContext):
    await state.finish()

    await message.answer(text="<b>Kerakli bo'limni tanlang 👇</b>",
        reply_markup=menu_btn(message.from_user.id))


# Change city
@dp.message_handler(lambda message: not str(message.chat.id).startswith("-"), text=["📍 Shaharni o'zgartirish"], state=SettingsState.command)
async def change_city_handler(message: types.Message, state: FSMContext):
    msg = await message.answer("ㅤ", reply_markup=types.ReplyKeyboardRemove())
    await msg.delete()

    await SettingsState.change_city.set()
    await message.answer("<b>Kerakli xududni tanlang 👇</b>", reply_markup=regions_btn(current_page=0))


# Select City
@dp.callback_query_handler(lambda call: not str(call.message.chat.id).startswith("-"), text=REGIONS, state=SettingsState.change_city)
async def prayer_times_handler(call: types.CallbackQuery, state: FSMContext):
    try:
        update_user_region(user_id=call.from_user.id, region=call.data)
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f"<b>Hududingiz {call.data} ga o'zgartirildi ✅</b>", reply_markup=back_btn)
    except:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                text=f"""<b>Xatolik yuz berdi ❌</b>""", reply_markup=back_btn)

# Next / Back
@dp.callback_query_handler(lambda call: not str(call.message.chat.id).startswith("-"), lambda call: str(call.data).startswith('next_') or str(call.data).startswith('back_'), state=SettingsState.change_city)
async def city_change_page_handler(call: types.CallbackQuery):
    if call.data.startswith('next_'):
        page = int(call.data.split('_')[1])

        if not page == 7:
            msg_id = call.message.message_id
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, 
                                                reply_markup=regions_btn(current_page=page))
    else:
        page = int(call.data.split('_')[1])

        if not page == -1:
            msg_id = call.message.message_id
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, 
                                                reply_markup=regions_btn(current_page=page))


# Back to settings
@dp.callback_query_handler(lambda call: not str(call.message.chat.id).startswith("-"), text=['backto_prayer_time'], state=SettingsState.change_city)
async def back_prayer_handler(call: types.CallbackQuery, state: FSMContext):
    user = get_user(user_id=call.from_user.id)
    await call.message.delete()

    await SettingsState.command.set()
    await call.message.answer("<b>Kerakli bo'limni tanlang 👇</b>", 
                              reply_markup=settings_btn(notification=user.json()['notification']))
    

# Back to main menu
@dp.callback_query_handler(lambda call: not str(call.message.chat.id).startswith("-"), text=['backto_menu'], state=SettingsState.change_city)
async def back_menu_handler(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    
    await call.message.answer(text="<b>Kerakli bo'limni tanlang 👇</b>",
        reply_markup=menu_btn(call.from_user.id))
    

# On/Off notification
@dp.message_handler(lambda message: not str(message.chat.id).startswith("-"), text=["🔔 Bildirishnomani yoqish", "🔕 Bildirishnomani o'chirish"], state=SettingsState.command)
async def off_on_notification(message: types.Message, state: FSMContext):
    user = get_user(user_id=message.from_user.id)

    if user.status_code == 200:
        if (user.json()['notification']) and message.text == "🔕 Bildirishnomani o'chirish":
            update_user_notification(user_id=message.from_user.id, notification=False)
            await message.answer(f"<b>Bildirishnoma o'chirildi 🔕</b>", reply_markup=settings_btn(notification=False))
        elif (not user.json()['notification']) and message.text == "🔔 Bildirishnomani yoqish":
            update_user_notification(user_id=message.from_user.id, notification=True)
            await message.answer(f"<b>Bildirishnoma yoqildi 🔔</b>", reply_markup=settings_btn(notification=True))