import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

REFS = {
    "mono": "https://YOUR_MONO_LINK",
    "privat": "https://YOUR_PRIVAT_LINK",
    "pumb": "https://YOUR_PUMB_LINK"
}

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Monobank")],
        [KeyboardButton(text="PrivatBank")],
        [KeyboardButton(text="PUMB")]
    ],
    resize_keyboard=True
)

@dp.message()
async def handle(message: types.Message):
    if message.text == "/start":
        await message.answer("👋 Привет! Выбери банк:", reply_markup=menu)

    elif message.text == "Monobank":
        await message.answer(REFS["mono"])

    elif message.text == "PrivatBank":
        await message.answer(REFS["privat"])

    elif message.text == "PUMB":
        await message.answer(REFS["pumb"])

    else:
        await message.answer("Нажми /start")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
