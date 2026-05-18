import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🔗 РЕФЕРАЛЬНЫЕ ССЫЛКИ
REFS = {
    "mono": "https://monobank.ua/r/Sya4uw",
    "privat": "https://www.privat24.ua/invite/j7r1p",
    "pumb": "https://pumb.onelink.me/Jrxy/875acyqw",
    "a_bank": "https://link.a-bank.com.ua/JWUdopdB"
}

# 🔘 КНОПКИ МЕНЮ
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Монобанк")],
        [KeyboardButton(text="ПриватБанк")],
        [KeyboardButton(text="ПУМБ")],
        [KeyboardButton(text="A-Bank")]
    ],
    resize_keyboard=True
)

# 💬 ОБРАБОТКА СООБЩЕНИЙ
@dp.message()
async def handle(message: types.Message):

    if message.text == "/start":
        await message.answer(
            "👋 Привіт! Обери банк та отримай бонус 👇",
            reply_markup=menu
        )

    elif message.text == "Монобанк":
        await message.answer(REFS["mono"])

    elif message.text == "ПриватБанк":
        await message.answer(REFS["privat"])

    elif message.text == "ПУМБ":
        await message.answer(REFS["pumb"])

    elif message.text == "A-Bank":
        await message.answer(REFS["a_bank"])

    else:
        await message.answer("Натисни /start щоб почати 👇")


# 🌐 WEBHOOK SERVER (Render)
async def handle_webhook(request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return web.Response()


async def on_startup():
    webhook_url = os.getenv("WEBHOOK_URL")
    await bot.set_webhook(f"{webhook_url}/webhook")


async def main():
    app = web.Application()
    app.router.add_post("/webhook", handle_webhook)

    await on_startup()

    return app


if __name__ == "__main__":
    web.run_app(main(), host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
