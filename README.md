# ---------------------------------------
# 🏛️ v6.0 APPROVAL GATEWAY (HUMAN-IN-THE-LOOP)
# ---------------------------------------
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = 'YOUR_BOT_TOKEN'
ADMIN_ID = 123456789 # আপনার টেলিগ্রাম আইডি
bot = telebot.TeleBot(TOKEN)

class ApprovalGateway:
    def __init__(self):
        self.pending_tasks = {}

    def request_permission(self, content_type, data):
        """
        এআই কোনো পোস্ট বা ভিডিও বানালে এই ফাংশনটি কল করবে।
        """
        task_id = hash(data)
        self.pending_tasks[task_id] = data
        
        # টেলিগ্রামে বাটন পাঠানো
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("✅ Approve & Publish", callback_data=f"publish_{task_id}"),
            InlineKeyboardButton("❌ Reject & Delete", callback_data=f"reject_{task_id}")
        )
        
        msg = f"🛰️ **AI v6.0 Proposal:**\nType: {content_type}\nContent: {data[:100]}..."
        bot.send_message(ADMIN_ID, msg, reply_markup=markup, parse_mode="Markdown")
        print(f"⏳ Waiting for Human Approval for Task: {task_id}")

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    action, task_id = call.data.split("_")
    
    if action == "publish":
        # এখানে YouTube/Facebook API কল করার কোড থাকবে
        bot.answer_callback_query(call.id, "🚀 Publishing to Social Media...")
        bot.edit_message_text("✅ Task Approved and Published!", call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "🗑️ Task Discarded.")
        bot.edit_message_text("❌ Task Rejected by User.", call.message.chat.id, call.message.message_id)

# ব্যবহারের নিয়ম:
# gateway = ApprovalGateway()
# gateway.request_permission("Facebook Post", "Hello World from AI v6.0!")