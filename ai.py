import telebot
import google.generativeai as genai

# مقادیر اصلی
BOT_TOKEN = '802549012:2SglERgmkafn0HTTh7w8fT304wREI_LUCFs' 
GOOGLE_API_KEY = "AIzaSyDtTMrU6G8_ZJG5OXrQVCX-RE989YFn9s0"

# تنظیمات هوش مصنوعی
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# تنظیمات بله (اضافه کردن آدرس بله)
bot = telebot.TeleBot(BOT_TOKEN, base_url="https://api.ble.ir/bot")

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        # فرستادن پیام به هوش مصنوعی
        response = model.generate_content(message.text)
        # جواب هوش مصنوعی به کاربر در بله
        bot.reply_to(message, response.text)
        print(f"✅ پاسخ هوش مصنوعی ارسال شد به: {message.text}")
    except Exception as e:
        print(f"❌ خطا در پاسخگویی: {e}")

print("🚀 هوش مصنوعی علیرضا در بله فعال شد!")
bot.polling()
