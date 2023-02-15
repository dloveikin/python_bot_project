''' Створення екземплярів боту і диспечера для подальших імпортів'''
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from token_key import api_token

# Initialize bot and dispatcher
bot = Bot(token=api_token)
dp = Dispatcher(bot)