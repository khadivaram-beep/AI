import telebot
import google.generativeai as genai

# ۱. اطلاعات اصلی (بدون دستکاری)
BOT_TOKEN = '802549012:2SglERgmkafn0HTTh7w8fT304wREI_LUCFs' 
GOOGLE_API_KEY = "AIzaSyDtTMrU6G8_ZJG5OXrQVCX-RE989YFn9s0"

# ۲. راه‌اندازی جمینای
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# ۳. تنظیمات بله (با دقت بالا)
# علیرضا، اگه قبلاً با "base_url" جواب می‌گرفتی، اینجا رو دقت کن:
bot = telebot.TeleBot(BOT_TOKEN)
telebot.apihelper.API_URL = "https://api.ble.ir/bot{0}/{1}"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        # دریافت پیام
        user_input = message.text
        print(f"📥 پیام از بله: {user_input}")
        
        # تولید پاسخ توسط هوش مصنوعی
        ai_response = model.generate_content(user_input)
        
        # ارسال به بله
        bot.reply_to(message, ai_response.text)
        print("✅ پاسخ ارسال شد.")
        
    except Exception as e:
        print(f"❌ خطای لحظه‌ای: {e}")

# ۴. بخش حیاتی: استارت ربات بدون چک کردن وضعیت (Skip getMe)
print("🔥 علیرضا، کد بازنویسی شد. دارم استارت می‌زنم...")

# این متد اجازه می‌ده ربات بدون توجه به ارور ۴۰۴ در شروع، کارش رو انجام بده
bot.infinity_polling(timeout=10, long_polling_timeout=5)
