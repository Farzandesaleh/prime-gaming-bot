import asyncio
from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError

TOKEN = '8166528889:AAGECe1AznUADZ26WQFTYloHURtAqHb_y6Y'
CHAT_ID = '379260580'

bot = Bot(token=TOKEN)

async def get_prime_gaming_news():
    message = (
        "🎮 Prime Gaming Alert!\n"
        "بازی‌های رایگان جدید Prime Gaming رو چک کن: https://gaming.amazon.com\n"
        "✅ هر ماه آپدیت جدید، بازی‌های رایگان و آیتم‌های داخل بازی فقط برای Prime Memberها!\n"
        "🔥 سریع claim کن تا از دستت نرفته!"
    )
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)
        print("✅ پیام ارسال شد!")
    except TelegramError as e:
        print(f"❗ خطا هنگام ارسال پیام: {e}")

async def scheduler():
    while True:
        now = asyncio.get_event_loop().time()
        target = now + (60 - (now % 60))  # اجرای هر دقیقه (میتونی زمان‌بندی دقیق‌تر بنویسی)
        await asyncio.sleep(target - now)
        # فقط برای تست: هر دقیقه پیام می‌فرسته
        await get_prime_gaming_news()

if __name__ == '__main__':
    asyncio.run(scheduler())
