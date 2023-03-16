import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_one = types.KeyboardButton("CV in Russian")
    item_two = types.KeyboardButton("Experience")
    item_free = types.KeyboardButton("CV in English")
    item_foo = types.KeyboardButton("Project")
    item_five = types.KeyboardButton("Skills")
    item_six = types.KeyboardButton("Company")
    markup.add(item_one, item_two, item_free, item_foo, item_five, item_six)
    sti = open('static/photo_2022-12-31_13-06-16.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Welcome, {0.first_name}!'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def output(message):
    if message.chat.type == 'private':
        if message.text == 'CV in Russian':
            cv = open('static/Taras.pdf', 'rb')
            bot.send_document(message.chat.id, cv)
        elif message.text == 'Experience':
            bot.send_message(message.chat.id, 'Anybots Bali, anybots.ru'
                                              'интеграция, интернет'
                                              'Full-stack разработчик (full-time)'
                                              '1. разработка телеграмм ботов на '
                                              'node.js'.format(message.from_user, bot.get_me(), parse_mode="markup"))


bot.polling(none_stop=True)
