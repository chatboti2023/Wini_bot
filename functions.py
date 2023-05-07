# libs
from aiogram import *
from aiogram.types import *
import data_base, random, asyncio, api

# functions
async def start_func(message):
    ReplyKeyboardRemove()

    start_message = f"""
Добро пожаловать, {message.from_user.first_name}!

Это бот взаимоподписки. Функционал бота является платным, но для вас бесплатный период 14 дней.

Для того, чтобы пользоваться бесплатно, необходимо пригласить 10 последователей
    """

    if data_base.id_list.count(message.from_user.id) == 0:
        buttons = ReplyKeyboardMarkup(resize_keyboard = True)

        profile_button = KeyboardButton("Личный кабинет")
        help_button = KeyboardButton("Помощь")
        buttons.add(profile_button, help_button)

        await message.answer(start_message, reply_markup = buttons)

        referal_code = random.randint(1000, 9999)
        referal_code = str(referal_code) + str(len(data_base.id_list))

        await data_base.started(message, referal_code)
            
        await message.answer(f"Ваш реферальнный код: {referal_code}")
    else:
        await message.answer("Мы рады, что вы к нам вернулись!")


async def home_func(message):
    buttons = ReplyKeyboardMarkup(resize_keyboard = True)

    profile_button = KeyboardButton("Личный кабинет")
    help_button = KeyboardButton("Помощь")
    buttons.add(profile_button, help_button)

    await message.answer("Вы на главной странице", reply_markup = buttons)


async def add_chanel_func(message):
    url = message.text[12:]

    if data_base.chanels_list.count(url) == 0:
        await data_base.add_chanel(url, message.from_user.id)

        for i in range(len(data_base.id_list)):
            await api.api_bot.send_message(data_base.id_list[i], f"Новый канал: {url}")


async def add_city_func(message):
    city = message.text[6:]

    await data_base.update("users", "Город", "ID", city, message.from_user.id)


async def add_referal_func(message):
    code = message.text[9:]

    user_index = data_base.id_list.index(message.from_user.id)
    referal_user_index = data_base.users_ref_list.index(int(code))

    if data_base.users_ref_list.count(int(code)) != 0 and data_base.ref_list[user_index] == "нет" and code != data_base.users_ref_list[user_index]:
        await data_base.update("users", "Пригласительный_реферальный_код", "ID", code, message.from_user.id)
        await data_base.update("users", "Баланс", "Ваш_реферальный_код", int(data_base.money_list[referal_user_index]) + 5, code)


async def get_profile_func(message):
    user_index = data_base.id_list.index(message.from_user.id)

    text = f"""
Ваш профиль:
ID - {data_base.id_list[user_index]}
Реферальный код - {data_base.users_ref_list[user_index]}
Город - {data_base.home_list[user_index]}
Алмазы - {data_base.money_list[user_index]}
    """

    await message.answer(text)


async def sub_func(message):
    text = f"""
    функция находится в разработке :|
    """

    await message.answer(text)    


async def check_chanel_func(message):
    await message.answer("Это ваши каналы:")
    
    await data_base.get_chanel(message.from_user.id)
    
    for i in range(len(data_base.chanels_to_bot)):
        await message.answer(data_base.chanels_to_bot[i][0])


async def help_func(message):
    text = f"""
чтобы окончательно пройти регистрацию, добавьте город и каналы.

/chanel_<ссылка на канал> - добавить канал
/add_city_<имя города/населенного пункта> - установить своё место

если у вас есть реферальный код, то вы сможете его активировать командой

/referal_<код>
___
🆘

Вся информация находиться по адресу

avto-podpiska.ru (пока не работает)

При возникновении ошибок 
- при оплате
- неправильной работе бота
- проблем с сервером и т.д.
Обращайтесь к нашим админам:
@alexmatorkin

Ваши обращения будут обрабатываться быстрее если будет прикладывать скрины ваших проблем!
___
    """

    await message.answer(text)

async def profile_func(message):
    ReplyKeyboardRemove()
    
    buttons = ReplyKeyboardMarkup(resize_keyboard = True)
    me_button = KeyboardButton("Профиль")
    chanel_button = KeyboardButton("Каналы")
    sub_button = KeyboardButton("Подписка")
    home_button = KeyboardButton("Домой")
    
    buttons.add(me_button, chanel_button)
    buttons.add(sub_button)
    buttons.add(home_button)
    
    await message.answer("Открываем личный кабинет", reply_markup = buttons)