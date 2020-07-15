from aiogram import types

test_keyboard = types.InlineKeyboardMarkup(row_width=1)
test_button = types.InlineKeyboardButton(text="Сделать...", callback_data="todo")

test_keyboard.add(test_button)