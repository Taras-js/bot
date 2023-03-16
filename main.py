import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_one = types.KeyboardButton("CV in Russian")
    item_two = types.KeyboardButton("Projects")
    item_free = types.KeyboardButton("Github")
    item_foo = types.KeyboardButton("CV in English")
    item_five = types.KeyboardButton("Gitlab")
    item_six = types.KeyboardButton("Skills")
    markup.add(item_one, item_two, item_free, item_foo, item_five, item_six)
    sti = open('static/images.jpg', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Welcome, {0.first_name}!'.format(message.from_user, bot.get_me()),
                     parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def output(message):
    if message.chat.type == 'private':
        if message.text == 'CV in Russian':
            cv = open('static/Taras.pdf', 'rb')
            bot.send_document(message.chat.id, cv)
        if message.text == 'CV in English':
            cv = open('static/Taras_cv.pdf', 'rb')
            bot.send_document(message.chat.id, cv)
        if message.text == 'Projects':
            bot.send_message(message.chat.id, f'site: https://taras-server.ru/  \n bot: https://t.me/Demo_auto_bot'
                             .format(message.from_user, bot.get_me(), parse_mode="markup"))
        if message.text == 'Github':
            bot.send_message(message.chat.id, 'https://github.com/Taras-js'.format(message.from_user, bot.get_me(),
                                                                                   parse_mode="markup"))
        if message.text == 'Skills':
            cv = open('static/scills.webp', 'rb')
            bot.send_document(message.chat.id, cv)
        if message.text == 'Gitlab':
            bot.send_message(message.chat.id, 'https://gitlab.com/Taras-JS'.format(message.from_user, bot.get_me(),
                                                                                   parse_mode="markup"))


bot.polling(none_stop=True)
