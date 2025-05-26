import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError

TOKEN = '8166528889:AAGECe1AznUADZ26WQFTYloHURtAqHb_y6Y'
CHAT_ID = '379260580'

bot = Bot(token=TOKEN)

async def send_daily_reminder():
    message = (
        "🎮 <b>یادآوری روزانه Prime Gaming</b>\n"
        "هر روز چک کن که بازی‌های رایگان جدید چی اومده! 👇\n"
        "https://gaming.amazon.com/home"
    )
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)
        print("✅ پیام یادآوری ارسال شد!")
    except TelegramError as e:
        print(f"❗ خطا هنگام ارسال پیام: {e}")

async def scheduler():
    while True:
        await send_daily_reminder()
        await asyncio.sleep(60 * 60 * 24)  # هر 24 ساعت یک بار

if __name__ == '__main__':
    asyncio.run(scheduler())
