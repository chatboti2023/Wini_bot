# libs
from aiogram import *
from aiogram.types import *

def BOT(TOKEN):
    global api_bot, api_bot_dispetcher

    api_bot = Bot(TOKEN)
    api_bot_dispetcher = dispatcher.Dispatcher(api_bot)

async def COMMAND(message, text, command, event):
    if text == command:
        await event(message)