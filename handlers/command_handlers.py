from aiogram.types import Message

from keyboards.reply import start_keyboard
from loader import dp


@dp.message_handler(commands=["start"])
async def start(message: Message):
    start_text = "ToDo menu"
    await message.answer(text=start_text, reply_markup=start_keyboard)


@dp.message_handler(commands=["help", "info"])
async def help_info(message: Message):
    info_text = "ToDoBot поможет вам спланировать задачи на каждый день"
    await message.answer(text=info_text)
