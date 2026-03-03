import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import ADMIN_ID
from database import Database

db = Database()

def setup_bot(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, "مرحباً بك في البوت 👋")

    @bot.message_handler(commands=['withdraw'])
    def withdraw(message):
        user_id = message.from_user.id
        user = db.get_user(user_id)

        if not user or user['balance_available'] < 0.03:
            bot.send_message(message.chat.id, "❌ رصيدك غير كافي (الحد الأدنى 0.03 TON)")
            return

        if db.has_pending_withdrawal(user_id):
            bot.send_message(message.chat.id, "⏳ لديك طلب قيد الانتظار.")
            return

        msg = bot.send_message(message.chat.id, "💳 أرسل عنوان محفظتك:")
        bot.register_next_step_handler(msg, process_wallet)

    def process_wallet(message):
        wallet = message.text.strip()
        msg = bot.send_message(message.chat.id, "💰 أدخل مبلغ السحب:")
        bot.register_next_step_handler(msg, process_amount, wallet)

    def process_amount(message, wallet):
        user_id = message.from_user.id
        try:
            amount = float(message.text)
        except:
            bot.send_message(message.chat.id, "❌ أدخل رقم صحيح.")
            return

        user = db.get_user(user_id)

        if amount < 0.03 or amount > user['balance_available']:
            bot.send_message(message.chat.id, "❌ مبلغ غير صالح.")
            return

        db.create_withdrawal(user_id, amount, wallet)
        bot.send_message(message.chat.id, "✅ تم إرسال طلب السحب للإدارة.")
        bot.send_message(ADMIN_ID, f"طلب سحب جديد\nUser: {user_id}\nAmount: {amount}\nWallet: {wallet}")
