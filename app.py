from flask import Flask, request
import telebot
from config import TOKEN, DOMAIN
from bot import setup_bot  # ملف bot.py فيه دالة setup_bot التي تضبط handlers

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)
setup_bot(bot)

# نقطة استقبال Webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    # إزالة أي Webhook سابق
    bot.remove_webhook()
    # تعيين Webhook جديد على رابط Railway
    bot.set_webhook(url=f"{DOMAIN}/{TOKEN}")
    print("Bot webhook is set, Flask app is running...")
    # تشغيل Flask على المنفذ 8000 كما يطلب Railway
    app.run(host="0.0.0.0", port=8000)