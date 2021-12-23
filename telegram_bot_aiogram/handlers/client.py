from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Здравствуйте! Вас приветствует бот-помощник аэропорта Газолин! '
                                                     'Что бы Вы хотели узнать?', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему')


#@dp.message_handler(commands=['Режим_работы'])
async def airport_open_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Круглосуточно')


#@dp.message_handler(commands=['Адрес_аэропорта'])
async def airport_adress(message: types.Message):
    await bot.send_message(message.from_user.id, 'Аэропорт Газолин, Грушевский район')


async def airport_information(message: types.Message):
    await bot.send_message(message.from_user.id, '\nИНФОРМАЦИЯ ОБ АЭРОПОРТЕ:\n'

                                                 '\n - Аэропорт Газолин, Грушевский район'
                                                 '\n - Дата основания: 12.12.2001 г.'
                                                 '\n - Годовой пассажиропоток: 55 млн. пассажиров в год'
                                                 '\n - Количество терминалов: 3'

                                                 '\nТЕРМИНАЛЫ:\n'

                                                 '\n 1. Терминал A:\n'
                                                 '\n - Дата основания: 12.12.2001 г.'
                                                 '\n - Годовой пассажиропоток: 15 млн. пассажиров в год'
                                                 '\n - Количество телетрапов: 9'
                                                 '\n - Количество стоянков: 10'
                                                 '\n - Принимаемые воздушные суда:'
                                                 '\n a. Airbus A 319/320/321/320 NEO/321 NEO/340/350'
                                                 '\n b. Boeing 737/747/777/787'
                                                 '\n - Для международных полетов'

                                                 '\n 2. Терминал B:\n'
                                                 '\n - Дата основания: 08.06.2011 г.'
                                                 '\n - Годовой пассажиропоток: 30 млн. пассажиров в год'
                                                 '\n - Количество телетрапов: 5'
                                                 '\n - Количество стоянков: 8'
                                                 '\n - Принимаемые воздушные суда:'
                                                 '\n a. Airbus A 319/320/321/320 NEO/321 NEO/340/350'
                                                 '\n b. Boeing 737/747/777/787'
                                                 '\n - Для международных полетов'

                                                 '\n 2. Терминал C:\n'
                                                 '\n - Дата основания: 13.06.2021 г.'
                                                 '\n - Годовой пассажиропоток: 10 млн. пассажиров в год'
                                                 '\n - Количество телетрапов: 11'
                                                 '\n - Количество стоянков: 15'
                                                 '\n - Принимаемые воздушные суда:'
                                                 '\n a. Airbus A 319/320/321/320 NEO/321 NEO/340/350'
                                                 '\n b. Boeing 737/747/777/787'
                                                 '\n - Для внутренних полетов')

@dp.message_handler(commands=['Самолеты'])
async def info_planes(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(airport_open_start, commands=['Режим_работы'])
    dp.register_message_handler(airport_adress, commands=['Адрес'])
    dp.register_message_handler(airport_information, commands=['Информация'])
    dp.register_message_handler(info_planes, commands=['Самолеты'])