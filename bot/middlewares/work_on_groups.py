from aiogram import types, Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler


class WorkOnlyPrivateChats(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        if str(message.chat.id).startswith("-"):
            raise CancelHandler