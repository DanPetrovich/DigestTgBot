from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
from aiogram import types
import logging
import config
import random
import keyboard

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=config.bot_token)
dp = Dispatcher(bot, storage=storage)

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


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    output = f'Привет, {message.from_user.first_name} {message.from_user.last_name}, рад видеть тебя!'



    await message.answer(text=output, reply_markup=keyboard.menu_markup)


@dp.message_handler(content_types='text', text='О боте')
async def help_def(message):
    output = f'Позволь представится, я бот на 7/10. Могу кинуть тебе ссылку на спорт канал;)'
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Выбрать спорт')
async def choose_sport(message):
    await message.answer(text='Выберите спорт', reply_markup=keyboard.sport_markup)


@dp.message_handler(content_types='text', text='Информация')
async def get_info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('О боте')
    back = types.KeyboardButton('Назад')
    markup.add(item1, back)
    await message.answer(text='Информация', reply_markup=markup)


@dp.message_handler(content_types='text', text='Назад')
async def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = [types.KeyboardButton('Выбрать спорт'),
            types.KeyboardButton('Информация'),
            types.KeyboardButton('Получить рандомную ссылку')]
    for item in menu:
        markup.add(item)
    await message.answer(text='Назад', reply_markup=markup)


@dp.message_handler(content_types='text', text='Футбол')
async def football(message):
    output = sports[message.text]
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Баскетбол')
async def basketball(message):
    output = sports[message.text]
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Хоккей')
async def hockey(message):
    output = sports[message.text]
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Волейбол')
async def volleyball(message):
    output = sports[message.text]
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Большой теннис')
async def tennis(message):
    output = sports[message.text]
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Гандбол')
async def gandball(message):
    output = sports[message.text]
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Мини-футбол')
async def mini_football(message):
    output = sports[message.text]
    await message.answer(text=output)

@dp.message_handler(content_types='text', text='UFC')
async def ufc(message):
    output = sports[message.text]
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Бокс')
async def box(message):
    output = sports[message.text]
    await message.answer(text=output)

@dp.message_handler(content_types='text', text='Регби')
async def regbi(message):
    output = sports[message.text]
    await message.answer(text=output)

@dp.message_handler(content_types='text', text='Получить рандомную ссылку')
async def random_link(message):
    output = random.choice(list(sports.keys()))
    await message.answer(text=sports[output])


@dp.message_handler()
async def button_message(message):
    if message.text.lower() in ["привет", 'добрый день']:
        output = 'привет!'
    elif message.text[-1] == '?':
        output = 'Введите /help, чтобы получить инфу или выберите спорт, чтоб получить новости'
    else:
        output = 'Да, в целом, ты прав, но я тактично промолчу'
        await message.answer(text=output)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
