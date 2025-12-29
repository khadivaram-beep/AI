import telebot
import google.generativeai as genai

# ۱. توکن بله را اینجا بگذار
BOT_TOKEN = 'توکن_بله_خودت_را_اینجا_بنویس' 

# ۲. کلید گوگل
GOOGLE_API_KEY = "AIzaSyDtTMrU6G8_ZJG5OXrQVCX-RE989YFn9s0"

# تنظیمات اصلی
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "سلام!\nمن یک هوش مصنوعی هستم.\n👨‍💻 طراحی شده توسط: علیرضا خدیور")

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        # ارسال مستقیم پیام به گوگل
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "مشکلی در اتصال به هوش مصنوعی پیش آمد.")

print("🚀 ربات با موفقیت توسط علیرضا خدیور اجرا شد...")
bot.polling()
