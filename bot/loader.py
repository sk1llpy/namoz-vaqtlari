from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config


dp = Dispatcher(
    bot = Bot(
        token = config.BOT_TOKEN,
        parse_mode = types.ParseMode.HTML
    ),
    storage = MemoryStorage()
)
bot = dp.bot