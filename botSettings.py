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

athletes = {'Футбол': 'https://metaratings.ru/upload/iblock/736/73683ca7f4dace7a941c9dfd3b75737b.jpg',
          'Баскетбол': 'https://www.vladtime.ru/uploads/posts/2017-02/1487312286_i.jpeg',
          'Хоккей': 'https://stavkinasport.com/wp-content/uploads/post/81988/ovie.jpg',
          'Волейбол': 'https://topcafe.su/wp-content/uploads/2019/04/Mari-Paraiba.jpg',
          'Большой теннис': 'https://fb.ru/media/i/1/5/2/6/3/6/4/i/1526364.jpg',
          'Гандбол': 'https://phototass2.cdnvideo.ru/width/1200_4ce85301/tass/m2/uploads/i/20191215/5280847.jpg',
          'Мини-футбол': 'http://sport.img.com.ua/nxs72/b/orig/c/28/63627c955c43a3ba49980f1896ddf28c.jpg',
          'UFC': 'https://odds.ru/upload/media/default/0001/91/035765a11d5ef989d575116f41e82aaac944baf7.jpg',
          'Бокс': 'https://citatnica.ru/wp-content/uploads/2019/06/Ali-1.jpg',
          'Регби': 'https://rugger.info/upload/images/Emily_Scarratt.jpeg'}


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
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Меня больше волнует быть хорошим человеком, чем быть "
                                                                 "лучшим футболистом в мире. Когда все это закончится, "
                                                                 "с чем же вы останетесь?")
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Баскетбол')
async def basketball(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Границы, так же как и страхи, "
                                                                 "чаще всего оказываются просто иллюзиями")
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Хоккей')
async def hockey(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="У меня к жизни отношение спортивное: "
                                                                 "если что-то не удается, это еще не значит, "
                                                                 "что этого не надо добиваться.")
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Волейбол')
async def volleyball(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Для игроков волейбол-это работа, "
                                                                 "Для «боссов» волейбол — это деньги, "
                                                                 "Для зрителей волейбол- это шоу, "
                                                                 "Для всех нас волейбол- это жизнь!")
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Большой теннис')
async def tennis(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Я никогда не сдаюсь. "
                                                                 "Вы можете сбить меня с ног десять раз подряд, "
                                                                 "и я поднимусь в одиннадцатый и запулю желтым "
                                                                 "мячиком прямо в вас. ")
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Гандбол')
async def gandball(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Если чего-то хочется, не люблю себе отказывать, "
                                                                 "больше даже в каком-то ментальном смысле, "
                                                                 "чтобы не стрессовать. Если чего-то хочется, "
                                                                 "то удовольствие, конечно, нужно получать.")
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Мини-футбол')
async def mini_football(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="В обычном футболе не всегда удается оценить талант, "
                                                                 "поскольку там важна и физическая готовность. "
                                                                 "В мини-футболе же большую роль играет техника, "
                                                                 "класс и тактические нюансы.")
    await message.answer(text=output)

@dp.message_handler(content_types='text', text='UFC')
async def ufc(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Когда я захожу в клетку, я представляю, "
                                                                 "будто это бой за пояс. Я не могу проиграть, "
                                                                 "если я проиграю, то потеряю всё. "
                                                                 "Я не имею права думать, что парень дебютант и "
                                                                 "бой будет лёгким. У меня нет таких мыслей. "
                                                                 "Я настраиваюсь на этот бой так же, как если бы "
                                                                 "моим соперником стал Серроне и Фергюсон.")
    await message.answer(text=output)


@dp.message_handler(content_types='text', text='Бокс')
async def box(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Чемпионами становятся не в тренажерных залах. "
                                                                 "Чемпиона рождает то, что у человека внутри — желания,"
                                                                 " мечты, цели.")
    await message.answer(text=output)

@dp.message_handler(content_types='text', text='Регби')
async def regbi(message):
    output = sports[message.text]
    picture = athletes[message.text]
    await bot.send_photo(message.chat.id, photo=picture, caption="Игроки в регби либо переворачивают пианино, "
                                                                 "либо передвигают пианино. К счастью, "
                                                                 "я одна из тех, кто может сыграть мелодию")
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
