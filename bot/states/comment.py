from aiogram.dispatcher.filters.state import State, StatesGroup

class Comment(StatesGroup):
    comment = State()