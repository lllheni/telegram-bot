import os
import telebot

TOKEN = os.getenv("8314831049:AAGWfyZ8IVQpQWzKduYTPdfeKA2hALgjwuM")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "✅ Bot is running!\nHello 👋"
    )

print("Bot started")
bot.infinity_polling()
