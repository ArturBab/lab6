from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

storage = MemoryStorage()

bot = Bot('5061919999:AAEoaBVZ99k49gLuYo0WOnlEwwtGzQ77XpQ')
dp = Dispatcher(bot, storage=storage)