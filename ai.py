import telebot
import google.generativeai as genai

# توکن بله و کلید گوگل
BOT_TOKEN = 'توکن_بله_شما'
GOOGLE_API_KEY = "AIzaSyDtTMrU6G8_ZJG5OXrQVCX-RE989YFn9s0"

# پیکربندی هوش مصنوعی
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    msg = (
        "🤖 بازوی هوشمند متصل به Gemini 1.5\n"
        "آماده پاسخگویی به سوالات شماست.\n\n"
        "👨‍💻 طراحی شده توسط: علیرضا خدیور"
    )
    bot.reply_to(message, msg)

@bot.message_handler(func=lambda message: True)
def handle_ai(message):
    try:
        # ارسال مستقیم به هوش مصنوعی و دریافت پاسخ
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, "خطا در اتصال به هوش مصنوعی!")

print("--- سیستم با موفقیت توسط علیرضا خدیور راه اندازی شد ---")
bot.polling()
