from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .work_on_groups import WorkOnlyPrivateChats


if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(WorkOnlyPrivateChats())