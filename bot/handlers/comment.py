from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from data.config import ADMINS
from states.comment import Comment as CommentState

from keyboards.reply.back import back_btn
from keyboards.reply.menu import menu_btn
from keyboards.inline.comment import user_btn


@dp.message_handler(text=["✍️ Izoh qoldirish"])
async def comment_handler(message: types.Message, state: FSMContext):
    await CommentState.comment.set()
    await message.answer("<b>Izoh qoldiring 👇</b>", reply_markup=back_btn)


@dp.message_handler(state=CommentState.comment)
async def comment_text_handler(message: types.Message, state: FSMContext):
    if not message.text == "⬅️ Orqaga":
        for admin in ADMINS:
            await bot.send_message(
                chat_id = admin,
                text = f"""<b>Yangi izox qoldirildi 💬</b>
                
<i>{message.text}</i>""",
                reply_markup = user_btn(
                    name = message.from_user.full_name,
                    username = message.from_user.username
                )
            )

            await state.finish()
            await message.answer("<b>Izoh yuborildi ✅</b>\n\n<i>Izoh qoldirganingiz uchun raxmat 😊</i>", 
                                 reply_markup=menu_btn(message.from_user.id))
    else:
        await state.finish()
        await message.answer(text="<b>Kerakli bo'limni tanlang 👇</b>",
        reply_markup=menu_btn(message.from_user.id))