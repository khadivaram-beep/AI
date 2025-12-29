import telebot
import google.generativeai as genai

# ۱. توکن بله رو با دقت اینجا بذار
BOT_TOKEN = 'توکن_بله_شما' 

# ۲. کلید گوگل
GOOGLE_API_KEY = "AIzaSyDtTMrU6G8_ZJG5OXrQVCX-RE989YFn9s0"

# تنظیمات
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "👨‍💻 طراحی شده توسط: علیرضا خدیور\nبه ربات هوش مصنوعی خوش آمدید. سوال خود را بپرسید:")

@bot.message_handler(func=lambda message: True)
def chat(message):
    print(f"📩 پیام جدید از بله: {message.text}") # برای اینکه توی ترمینال ببینی
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
        print("✅ پاسخ هوش مصنوعی ارسال شد.")
    except Exception as e:
        print(f"❌ خطا: {e}")
        bot.reply_to(message, "در حال حاضر مشکلی در اتصال به گوگل وجود دارد.")

print("🚀 سیستم آماده است. علیرضا جان، در بله پیام بده...")
bot.polling()
