import asyncio
import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError

TOKEN = '8166528889:AAGECe1AznUADZ26WQFTYloHURtAqHb_y6Y'
CHAT_ID = '379260580'

bot = Bot(token=TOKEN)

async def get_prime_gaming_news():
    try:
        response = requests.get('https://gaming.amazon.com/home')
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            game_sections = soup.find_all('div', class_='item-card')

            if not game_sections:
                message = "❗ نتوانستم بازی‌ها را پیدا کنم، ولی لینک اصلی: https://gaming.amazon.com/home"
            else:
                message = "🎮 <b>Prime Gaming بازی‌های رایگان امروز:</b>\n\n"
                for game in game_sections[:5]:  # فقط ۵ تا اول برای ساده‌سازی
                    title = game.find('h3').get_text(strip=True) if game.find('h3') else 'بدون عنوان'
                    image_tag = game.find('img')
                    image = image_tag['src'] if image_tag else ''
                    message += f"<b>{title}</b>\n{image}\n\n"
                message += "برای مشاهده بیشتر: https://gaming.amazon.com/home"
        else:
            message = "❗ خطا در دریافت لیست بازی‌ها از Prime Gaming."

        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)
        print("✅ پیام ارسال شد!")
    except Exception as e:
        print(f"❗ خطا هنگام ارسال پیام: {e}")

async def scheduler():
    while True:
        await get_prime_gaming_news()
        await asyncio.sleep(60 * 60 * 24)

if __name__ == '__main__':
    asyncio.run(scheduler())
