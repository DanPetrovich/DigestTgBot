import telebot as tb
from telebot import types
# import requests
import config

URL = config.URL
MyURL = config.bot_token

bot = tb.TeleBot(MyURL)

sports = {'Футбол': 'https://t.me/rflive',
          'Баскетбол': 'https://t.me/all_about_nba',
          'Хоккей': 'https://t.me/khl_official_telegram',
          'Волейбол': 'https://t.me/volleyVFV',
          'Большой теннис': 'https://t.me/elitetennis'}


@bot.message_handler(commands=['start'])
def start_def(message):
    output = f'Привет, <b>{message.from_user.id} {message.from_user.last_name}</b>'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    menu = [types.KeyboardButton('Выбрать спорт'),
            types.KeyboardButton('Информация')]

    for item in menu:
        markup.add(item)

    bot.send_message(message.chat.id, output, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_def(message):
    output = f'Я могу тебе скидывать еженедельную подборку спортивных новостей, ' \
             f'только выбери виды спорта, которые ты хочешь видеть в своей подборке'
    bot.send_message(message.chat.id, output, parse_mode='html')


@bot.message_handler()
def button_message(message):
    if message.text == 'Выбрать спорт':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu = []
        for s in sports.keys():
            menu.append(types.KeyboardButton(text=s))
        back = types.KeyboardButton('Назад')
        menu.append(back)
        for item in menu:
            markup.add(item)
        bot.send_message(message.chat.id, 'Выберите спорт', parse_mode='html', reply_markup=markup)
    elif message.text == 'Информация':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('О боте')
        back = types.KeyboardButton('Назад')
        markup.add(item1, back)
        bot.send_message(message.chat.id, 'Информация', parse_mode='html', reply_markup=markup)
    elif message.text == 'Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu = [types.KeyboardButton('Выбрать спорт'),
                types.KeyboardButton('Информация')]
        for item in menu:
            markup.add(item)
        bot.send_message(message.chat.id, 'Назад', parse_mode='html', reply_markup=markup)
    elif message.text == 'О боте':
        pass  # TODO
    elif message.text == 'Футбол':
        output = sports[message.text]
        bot.send_message(message.chat.id, output, parse_mode='html')  # TODO
    elif message.text == 'Баскетбол':
        output = sports[message.text]
        bot.send_message(message.chat.id, output, parse_mode='html')  # TODO
    elif message.text == 'Хоккей':
        output = sports[message.text]
        bot.send_message(message.chat.id, output, parse_mode='html')  # TODO
    elif message.text == 'Волейбол':
        output = sports[message.text]
        bot.send_message(message.chat.id, output, parse_mode='html')  # TODO
    elif message.text == 'Большой теннис':
        output = sports[message.text]
        bot.send_message(message.chat.id, output, parse_mode='html')  # TODO
    else:
        if message.text.lower() in ["привет", 'добрый день']:
            output = 'привет!'
        elif message.text[-1] == '?':
            output = 'Введите /help, чтобы получить инфу или выберите спорт, чтоб получить новости'
        else:
            output = 'Да, в целом, ты прав, но я тактично промолчу'

        bot.send_message(message.chat.id, output, parse_mode='html')

bot.polling(non_stop=True)
