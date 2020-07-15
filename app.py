from aiogram import  executor

from keyboards.reply import start_keyboard
from loader import bot
from data import admin_id


async def on_startup(dp):
    await bot.send_message(chat_id=admin_id, text="start polling", reply_markup=start_keyboard)


async def on_shutdown(dp):
    pass


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(dispatcher=dp, on_startup=on_startup)
