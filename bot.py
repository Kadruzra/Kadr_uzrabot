import os
import threading
from flask import Flask
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🎬 Kadr uzra botiga xush kelibsiz!\n\n"
        "Bu yerda qiziqarli kinolarni topishingiz mumkin."
    )


@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Xabaringiz qabul qilindi ✅")


@app.route("/")
def home():
    return "Kadr Uzra bot is running"


def run_bot():
    bot.infinity_polling()


if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
