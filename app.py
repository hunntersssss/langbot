import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiohttp import web

# Токен теперь берётся из переменных окружения Render
BOT_TOKEN = os.environ.get("8538385993:AAHsm8eodkpuRds9S89gWSu8Ek63mhTwZHg")

logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg: Message):
    await msg.answer(
        "🌍 <b>Language Training</b>\n\n"
        "Привет! Я помогу тебе практиковать иностранный язык.\n\n"
        "Напиши мне что-нибудь — я отвечу."
    )

@dp.message(F.text)
async def echo(msg: Message):
    await msg.answer(
        f"Ты написал: <b>{msg.text}</b>\n\n"
        "(Пока я просто повторяю. Скоро научусь отвечать и исправлять ошибки.)"
    )

async def handle(request):
    return web.Response(text="Bot is running")

async def main():
    # Запускаем простой веб-сервер для Render
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
    await site.start()
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())