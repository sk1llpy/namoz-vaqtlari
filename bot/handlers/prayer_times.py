from loader import dp, bot
from aiogram import types

from keyboards.reply.menu import menu_btn
from keyboards.inline.regions import button as regions_btn
from keyboards.inline.regions import button_week as regions_btn_week
from keyboards.inline.back import back_btn, back_btn_week

from functions.API.prayer_times.prayer_times import get_prayer_time, get_prayer_weekly_time
from data.regions import REGIONS
from text.text import PRAYER_TIME, PRAYER_TIME_WEEKLY


@dp.message_handler(text=['🧎 Namoz vaqtlari'])
async def prayer_times_handler(message: types.Message):
    msg = await message.answer("ㅤ", reply_markup=types.ReplyKeyboardRemove())
    await msg.delete()
    await message.answer("<b>Kerakli xududni tanlang 👇</b>", reply_markup=regions_btn(current_page=0, user_id=message.from_user.id))


@dp.message_handler(text=['📅 Haftalik taqvim']) 
async def prayer_times_week_handler(message: types.Message):
    msg = await message.answer("ㅤ", reply_markup=types.ReplyKeyboardRemove())
    await msg.delete()
    await message.answer("<b>Kerakli xududni tanlang 👇</b>", reply_markup=regions_btn_week(current_page=0, user_id=message.from_user.id))


@dp.callback_query_handler(lambda call: str(call.data).startswith('next_') or str(call.data).startswith('back_'))
async def page_handler(call: types.CallbackQuery):
    if call.data.startswith('next_'):
        page = int(call.data.split('_')[1])

        if not page == 7:
            msg_id = call.message.message_id
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, 
                                                reply_markup=regions_btn(current_page=page, user_id=call.from_user.id))
    else:
        page = int(call.data.split('_')[1])

        if not page == -1:
            msg_id = call.message.message_id
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, 
                                                reply_markup=regions_btn(current_page=page, user_id=call.from_user.id))
            

@dp.callback_query_handler(lambda call: str(call.data).startswith('nextweek_') or str(call.data).startswith('backweek_'))
async def page_handler(call: types.CallbackQuery):
    if call.data.startswith('nextweek_'):
        page = int(call.data.split('_')[1])

        if not page == 7:
            msg_id = call.message.message_id
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, 
                                                reply_markup=regions_btn_week(current_page=page, user_id=call.from_user.id))
    else:
        page = int(call.data.split('_')[1])

        if not page == -1:
            msg_id = call.message.message_id
            await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=msg_id, 
                                                reply_markup=regions_btn_week(current_page=page, user_id=call.from_user.id))


@dp.callback_query_handler(lambda call: str(call.data).endswith("_week") and str(call.data).split("_week")[0] in REGIONS)
async def prayer_times_weekly_handler(call: types.CallbackQuery):
    region = str(call.data).split("_week")[0]
    data = get_prayer_weekly_time(region)

    if data.status_code == 200:
        data = data.json()['data']

        try:
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text=PRAYER_TIME_WEEKLY(data=data),
                                    reply_markup=back_btn_week)
        except Exception as exc:
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f"""<b>{region} vaqti bo'yicha namoz vaqtlari topilmadi ❌</b>""", reply_markup=back_btn_week)
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f"""<b>{region} vaqti bo'yicha namoz vaqtlari topilmadi ❌</b>""", reply_markup=back_btn_week)


@dp.callback_query_handler(text=REGIONS)
async def prayer_times_handler(call: types.CallbackQuery):
    data = get_prayer_time(call.data)

    if data.status_code == 200:
        data = data.json()['data']

        try:
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text=PRAYER_TIME(date=data['date'],
                                                weekday=data['weekday'],
                                                hijri_date=data['hijri_date'],
                                                times=data['times'],
                                                region=call.data),
                                    reply_markup=back_btn)
        except:
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f"""<b>{call.data} vaqti bo'yicha namoz vaqtlari topilmadi ❌</b>""", reply_markup=back_btn)
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text=f"""<b>{call.data} vaqti bo'yicha namoz vaqtlari topilmadi ❌</b>""", reply_markup=back_btn)

    

@dp.callback_query_handler(text=['backto_prayer_time'])
async def back_prayer_handler(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="<b>Kerakli xududni tanlang 👇</b>",
        reply_markup=regions_btn(current_page=0, user_id=call.from_user.id)
    )


@dp.callback_query_handler(text=['backtoweek_prayer_time'])
async def back_prayer_week_handler(call: types.CallbackQuery):
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        text="<b>Kerakli xududni tanlang 👇</b>",
        reply_markup=regions_btn_week(current_page=0, user_id=call.from_user.id)
    )


@dp.callback_query_handler(text=['backto_menu'])
async def back_menu_handler(call: types.CallbackQuery):
    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id)
    
    await call.message.answer(text="<b>Kerakli bo'limni tanlang 👇</b>",
        reply_markup=menu_btn(call.from_user.id))