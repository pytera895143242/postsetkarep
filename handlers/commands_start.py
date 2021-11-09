import asyncio

from aiogram import types
from misc import dp,bot
import sqlite3
from .worktime import new_cout_posts,postind_v_setku

my_id = 1307813926

@dp.message_handler(commands=['admin'])
async def cmd_start(message: types.Message):
    if message.chat.id == my_id:
        from .worktime import count_posts
        await message.answer(f'Количество контента: {count_posts}')

@dp.message_handler(commands=['post'])
async def cmd_post(message: types.Message):
    if message.chat.id == my_id:
        await message.answer(text=f'Начинаю выкладывать посты')
        await postind_v_setku()
        await message.answer(text='Рассылка закончена')

@dp.message_handler(commands=['info'])
async def cmd_count_member(message: types.Message):
    if message.chat.id == my_id:
        await message.answer(text='Начинаю подсчет')
        from .worktime import setka
        pdp = 0
        for channel in setka:
            print(channel)
            pdp += int(await bot.get_chat_member_count(chat_id=channel[0]))
            await asyncio.sleep(3)
        await message.answer(f'Подписчиков в сетке: {pdp}\n'
                             f'Каналов 12 штук')


@dp.message_handler(content_types=['text'])
async def message_text(message: types.Message):
    if message.chat.id == my_id:
        try:
            int(message.text)
            await new_cout_posts(int(message.text))
            await message.answer(text=f'Новое количество контента обновлено до {message.text}')
        except:
            print('Не реагирую')