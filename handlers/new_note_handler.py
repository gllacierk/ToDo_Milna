
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from keyboards.reply import back_keyboard, start_keyboard
from loader import dp
from FSM import Note
from utils import data_cursor
import logging


@dp.message_handler(text="В главное меню", state="*")
async def in_main(message: Message, state: FSMContext):
    await message.answer(text="ToDo menu", reply_markup=start_keyboard)
    await state.reset_state()


@dp.message_handler(text="Создать новую заметку", state=None)
async def new_note_handler(message: Message):
    await message.answer(text="Введите название для новой заметки:", reply_markup=back_keyboard)
    await Note.NameNote.set()

    logging.info(msg="Waiting for a new note name")


@dp.message_handler(state=Note.NameNote)
async def note_name(message: Message, state: FSMContext):
    await message.answer(text="Теперь напишите что необходимо сделать")
    await Note.BodyNote.set()
    await state.update_data(name=message.text)

    logging.info(msg="Got a new note name")
    logging.info(msg="Waiting for a new note body")


@dp.message_handler(state=Note.BodyNote)
async def note_body(message: Message, state: FSMContext):
    await message.answer(text="Укажите дату для задачи")
    await Note.DateNote.set()
    await state.update_data(body=message.text)

    logging.info(msg="Got a new note body")
    logging.info(msg="Waiting for a new note date")


@dp.message_handler(state=Note.DateNote)
async def note_date(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    body = data.get("body")
    date = message.text

    await state.reset_state()
    await message.answer(text="Отлично, заметка создана!", reply_markup=start_keyboard)
    data_cursor.in_todo(user_id=message.from_user.id, note_name=name, note_body=body, note_date=date)

    logging.info(msg="Got a new note date")
