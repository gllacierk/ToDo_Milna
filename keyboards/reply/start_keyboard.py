from aiogram import types


start_keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
new_button = types.KeyboardButton(text="Создать новую заметку")
today_button = types.KeyboardButton(text="Посмотреть задачи на сегодня")
current_button = types.KeyboardButton(text="Посмотреть все задачи")
pass_button = types.KeyboardButton(text="Создать новую заметку")

start_keyboard.add(new_button, today_button, current_button)
