import telebot
import google.generativeai as genai

# ۱. توکن بازوی بله رو اینجا بین دوتا کوتیشن بذار
BOT_TOKEN = 'اینجا_توکن_بله_را_بنویس' 

# ۲. کلید گوگل (API Key) که با AIza شروع میشه رو اینجا بذار
GOOGLE_API_KEY = 'gen-lang-client-0088375120'

# تنظیمات هوش مصنوعی
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def chat_with_ai(message):
    try:
        # ارسال متن به گوگل
        response = model.generate_content(message.text)
        # فرستادن جواب به بله
        bot.reply_to(message, response.text)
    except Exception as e:
        print(f"Error: {e}")
        bot.reply_to(message, "بات متصل است اما کلید API گوگل نیاز به بررسی دارد.")

print("🚀 تبریک! بازو با موفقیت اجرا شد...")
bot.polling()
