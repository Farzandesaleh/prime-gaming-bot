# prime-gaming-bot```python
import requests
import telegram
import schedule
import time

TOKEN = '8166528889:AAGECe1AznUADZ26WQFTYloHURtAqHb_y6Y'
CHAT_ID = '379260580'

bot = telegram.Bot(token=TOKEN)

def get_prime_gaming_news():
    message = (
        "🎮 Prime Gaming Alert!\n"
        "بازی‌های رایگان جدید Prime Gaming رو چک کن: https://gaming.amazon.com\n"
        "✅ هر ماه آپدیت جدید، بازی‌های رایگان و آیتم‌های داخل بازی فقط برای Prime Memberها!\n"
        "🔥 سریع claim کن تا از دستت نرفته!"
    )
    bot.send_message(chat_id=CHAT_ID, text=message)

schedule.every().day.at("09:00").do(get_prime_gaming_news)

print("🤖 Prime Gaming Bot فعال شد و هر روز ساعت ۹ صبح پیام می‌فرسته!")

while True:
    schedule.run_pending()
    time.sleep(60)
```

✅ پس دو فایل نیاز داری:
1️⃣ main.py → همین کد بالا رو بذار توش.
2️⃣ requirements.txt → محتواش این باشه:
```
requests
python-telegram-bot==13.15
schedule
```
