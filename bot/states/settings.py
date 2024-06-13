from aiogram.dispatcher.filters.state import StatesGroup, State

class Settings(StatesGroup):
    command = State()
    change_city = State()