import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

# ВСТАВЬ СВОЙ ТОКЕН МЕЖДУ КАВЫЧКАМИ
BOT_TOKEN = ""

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

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
