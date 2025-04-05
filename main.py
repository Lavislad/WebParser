import telebot
from parser import parser
import re

token = '7827018602:AAH7ruDBiMDpmJnop0tWirxCvojStIUDP64'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['seturl'])
def take_url(message):
    bot.send_message(message.chat.id, 'Enter URL')

    @bot.message_handler(content_types=['text'])
    def take_url(message):
        global URL
        URL = message.text

    take_url(message)
    bot.send_message(message.chat.id, 'URL is set')

@bot.message_handler(commands=['currentURL'])
def send_last_news(message):
    bot.send_message(message.chat.id, URL)

bot.polling()