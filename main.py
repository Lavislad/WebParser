import telebot
from parser import parser
import re

token = '7827018602:AAH7ruDBiMDpmJnop0tWirxCvojStIUDP64'
bot = telebot.TeleBot(token)
URL = 'None'

@bot.message_handler(commands=['setURL'], content_types=['text'])
def take_url(message):
    bot.send_message(message.chat.id, 'Enter URL')

    def take_url(message):
        global URL
        URL = message.text

    take_url(message)
    bot.send_message(message.chat.id, 'URL is set')

@bot.message_handler(commands=['currentURL'])
def currentURL(message):
    bot.send_message(message.chat.id, URL)

@bot.message_handler(commands=['clearURL'])
def clearURL(message):
    global URL
    URL = 'None'
    bot.send_message(message.chat.id, 'URL has been cleared!')

bot.polling()