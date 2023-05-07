# libs
from aiogram import *
from aiogram.types import *
from functions import *
import api, data_base

# bot
api.BOT("5459716507:AAE51UZ8elcTjA1lkm2KL-MN8w0574Iz45w")

bot = api.api_bot
dp = api.api_bot_dispetcher

@dp.message_handler(content_types = ["text"])
async def messages(message: types.Message):

    await data_base.get_db()

    await api.COMMAND(message, message.text, command = "/start", event = start_func)

    await api.COMMAND(message, message.text, command = "Помощь", event = help_func)
    await api.COMMAND(message, message.text, command = "Личный кабинет", event = profile_func)
    await api.COMMAND(message, message.text, command = "Профиль", event = get_profile_func)
    await api.COMMAND(message, message.text, command = "Домой", event = home_func)
    
    await api.COMMAND(message, message.text, command = "Подписка", event = sub_func)
    await api.COMMAND(message, message.text, command = "Каналы", event = check_chanel_func)

    await api.COMMAND(message, message.text[:9], command = "/referal_", event = add_referal_func)
    await api.COMMAND(message, message.text[:6], command = "/city_", event = add_city_func)
    await api.COMMAND(message, message.text[:12], command = "/add_chanel_", event = add_chanel_func)

if __name__ == '__main__':
    executor.start_polling(dp)