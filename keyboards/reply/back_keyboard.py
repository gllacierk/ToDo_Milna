from aiogram import types

back_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton(text="В главное меню")

back_keyboard.add(back_button)
