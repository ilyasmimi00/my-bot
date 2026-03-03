from flask import Flask, request
import telebot
from config import TOKEN, DOMAIN
from bot import setup_bot

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)
setup_bot(bot)

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{DOMAIN}/{TOKEN}")
    app.run(host="0.0.0.0", port=8000)
