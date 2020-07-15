from aiogram.types import Message
from keyboards.inline import test_keyboard, current_note_keyboard
from loader import dp
from utils import data_cursor


@dp.message_handler(text="Посмотреть задачи на сегодня")
async def current_today_handler(message: Message):
    await message.answer(text="На сегодня вы запланировали:", reply_markup=test_keyboard)


@dp.message_handler(text="Посмотреть все задачи")
async def current_today_handler(message: Message):
    to_do = data_cursor.select_todo(column='note_name', user_id=message.from_user.id)
    print(to_do)
    if to_do is not None:
        for i in to_do:
            await message.answer(text=f"Все ваши заметки:\nЗаметка: {i} ", reply_markup=current_note_keyboard)

    elif to_do is None:
        await message.answer(text="Задач нет, создайте их")
