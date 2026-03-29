import telebot # pip install pyTelegramBotAPI
from safety.master_kill import KillSwitch # আগের কিল-সুইচটি ইম্পোর্ট করা হলো

# আপনার টেলিগ্রাম বট টোকেন এবং আপনার পার্সোনাল আইডি
TOKEN = 'YOUR_BOT_TOKEN'
ADMIN_ID = 123456789  # শুধুমাত্র আপনার আইডি থেকে কাজ করবে

bot = telebot.TeleBot(TOKEN)
k_switch = KillSwitch()

@bot.message_handler(commands=['kill_engine'])
def emergency_stop(message):
    if message.from_user.id == ADMIN_ID:
        bot.reply_to(message, "🚨 EMERGENCY RECEIVED! KILLING ALL AI PROCESSES... 💀")
        k_switch.manual_emergency_stop() # আগের কিল-সুইচ অ্যাক্টিভেট হবে
    else:
        bot.reply_to(message, "❌ ACCESS DENIED! YOU ARE NOT THE MASTER.")

print("📡 Telegram Kill-Switch is Online and Monitoring...")
bot.polling()