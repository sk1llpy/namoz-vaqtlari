from aiogram import executor
from loader import dp

import middlewares, handlers


if __name__ == '__main__':
    print("[INFO] BOT: Bot is running...")
    
    executor.start_polling(
        dispatcher = dp,
        skip_updates = True
    )