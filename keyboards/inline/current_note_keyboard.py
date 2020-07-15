from aiogram import types

current_note_keyboard = types.InlineKeyboardMarkup(resize_keyboard=True)
complete_button = types.InlineKeyboardButton(text="Выполнено", callback_data=f"complete")

current_note_keyboard.add(complete_button)
