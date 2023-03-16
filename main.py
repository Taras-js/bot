import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    sti = open('static/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, 'Welcome, <b>{0.first_name}!</b>'.format(message.from_user, bot.get_me()),
                     parse_mode="html")


@bot.message_handler(content_types=['text'])
def output(message):
    bot.send_message(message.chat.id, "Ты кто такой иди отсюда")


bot.polling(none_stop=True)
