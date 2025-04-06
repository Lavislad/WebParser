import telebot
from parser import parser
import re

token = '7827018602:AAH7ruDBiMDpmJnop0tWirxCvojStIUDP64'
bot = telebot.TeleBot(token)
URL = 'None'
waiting_for_url = False

@bot.message_handler(commands=['setURL'])
def handle_take_url(message):
    global waiting_for_url
    bot.send_message(message.chat.id, 'Enter URL')
    waiting_for_url = True

@bot.message_handler(func=lambda message: waiting_for_url, content_types=['text'])
def take_url(message):
    global URL, waiting_for_url
    URL = message.text
    bot.send_message(message.chat.id, 'URL is set')
    waiting_for_url = False

@bot.message_handler(commands=['currentURL'])
def currentURL(message):
    bot.send_message(message.chat.id, URL)

@bot.message_handler(commands=['clearURL'])
def clearURL(message):
    global URL
    URL = 'None'
    bot.send_message(message.chat.id, 'URL has been cleared!')

@bot.message_handler(commands=['parse'])
def handle_take_url(message):
    for i in range(parser(URL).get('Count')):
        bot.send_message(message.chat.id, parser('https://vlados.akeka.ru/news/').get(f'News {i + 1}').get('Title')+'\n'+parser('https://vlados.akeka.ru/news/').get(f'News {i + 1}').get('Date')+'\n'+parser('https://vlados.akeka.ru/news/').get(f'News {i + 1}').get('Full_text'))

bot.polling()