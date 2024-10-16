import telebot

# Replace with your bot token from BotFather
TOKEN = '7240905512:AAEYDNvLAOorSBQmLJRlXTahRkuGLoNPIgw'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет я тг бот")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()