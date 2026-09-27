import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "🎬 Kadr Uzra botiga xush kelibsiz!\n\n"
        "Bu yerda siz qiziqarli kinolarni topishingiz mumkin."
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Xabaringiz qabul qilindi ✅")

bot.infinity_polling()
