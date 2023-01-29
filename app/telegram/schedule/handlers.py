import telebot
from core.data import TOKEN


bot = telebot.TeleBot(token=TOKEN)


main_markup = telebot.types.ReplyKeyboardMarkup(True)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hey Daniel Here")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    print(message)
    bot.reply_to(message, message.text)
