from aiogram.dispatcher.filters.state import StatesGroup, State


class Note(StatesGroup):
    NameNote = State()
    BodyNote = State()
    DateNote = State()