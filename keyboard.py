from aiogram import types

sports = {'Футбол': 'https://t.me/rflive',
          'Баскетбол': 'https://t.me/all_about_nba',
          'Хоккей': 'https://t.me/khl_official_telegram',
          'Волейбол': 'https://t.me/volleyVFV',
          'Большой теннис': 'https://t.me/elitetennis',
          'Гандбол': 'https://t.me/rushandball',
          'Мини-футбол': 'https://t.me/futsal_rus',
          'UFC': 'https://t.me/UFCRussia',
          'Бокс': 'https://t.me/rcc_sport',
          'Регби': 'https://t.me/rugbyrussian'}

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
