from aiogram import types

from data import sports

menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
menu = [types.KeyboardButton('Выбрать спорт'),
        types.KeyboardButton('Информация'),
        types.KeyboardButton('Получить рандомную ссылку')]

for item in menu:
    menu_markup.add(item)

sport_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

menu = []
for s in sports.keys():
    menu.append(types.KeyboardButton(text=s))
back = types.KeyboardButton('Назад')
menu.append(back)
for item in menu:
    sport_markup.add(item)
