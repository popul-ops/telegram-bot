import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import web

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


async def on_startup(app):
    webhook_url = os.getenv("WEBHOOK_URL")
    await bot.set_webhook(f"{webhook_url}/webhook")


async def handle_webhook(request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return web.Response()


async def main():
    app = web.Application()
    app.router.add_post("/webhook", handle_webhook)

    await on_startup(app)

    return app


if __name__ == "__main__":
    web.run_app(main(), host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
