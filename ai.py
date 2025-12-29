import telebot
import sys

print("--- در حال تلاش برای روشن کردن ربات ---")

try:
    # توکن بله را اینجا بگذار
    token = 'توکن_بله_شما' 
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(func=lambda message: True)
    def echo(message):
        print(f"پیام دریافت شد: {message.text}")
        bot.reply_to(message, "سلام علیرضا! کد با موفقیت اجرا شد.")

    print("🚀 تبریک! ربات بدون مشکل روشن شد و منتظر پیام است...")
    bot.polling(non_stop=True)

except Exception as e:
    print(f"❌ خطای فوری: {e}")
