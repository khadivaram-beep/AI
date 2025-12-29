import telebot
import google.generativeai as genai

# ۱. مقادیر اصلی
BOT_TOKEN = '802549012:2SglERgmkafn0HTTh7w8fT304wREI_LUCFs' 
GOOGLE_API_KEY = "AIzaSyDtTMrU6G8_ZJG5OXrQVCX-RE989YFn9s0"

# ۲. تنظیمات هوش مصنوعی
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ۳. تنظیمات بله (اصلاح شده)
bot = telebot.TeleBot(BOT_TOKEN)
telebot.apihelper.API_URL = "https://api.ble.ir/bot{0}/{1}"

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        print(f"📩 پیام آمد: {message.text}")
        # گرفتن پاسخ از هوش مصنوعی
        response = model.generate_content(message.text)
        # فرستادن جواب به بله
        bot.reply_to(message, response.text)
        print("✅ پاسخ ارسال شد.")
    except Exception as e:
        print(f"❌ خطا: {e}")

print("🚀 تبریک! هوش مصنوعی علیرضا در بله بیدار شد...")
bot.polling()
