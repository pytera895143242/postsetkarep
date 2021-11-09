import datetime
import asyncio
import sqlite3
import random
from aiogram import types
from misc import dp,bot


channel_content = -1001734355893

start_count = 4 #4-17
count_posts = 17 #4-17


channel1 = [-1001458490452,'https://t.me/joinchat/Bp-FIO3mo_llOTBi'] #Самый главный канал
channel2 = [-1001387863196, 'https://t.me/joinchat/YLXFe-0rDo84NWYy']
channel3 = [-1001292379977, 'https://t.me/joinchat/ccspHmpblxM4MjRi']

channel4 = [-1001309736853,'https://t.me/joinchat/2LrCqE6UPSExM2Qy']
channel5 = [-1001473094572, 'https://t.me/joinchat/MPXapdHc5x41NWFi']
channel6 = [-1001277378424, 'https://t.me/joinchat/mb940FsP4Tk4MzRi']

channel7 = [-1001155163355, 'https://t.me/joinchat/oH-IY_DNrNQ0YjAy']
channel8 = [-1001187305514, 'https://t.me/joinchat/iargzLgAgtBhODFi']
channel9 = [-1001412761113,'https://t.me/joinchat/uYqRJUG9NC04MTg6']

channel10 = [-1001298169375, 'https://t.me/joinchat/5cOhyvewQFhjMTIy']
channel11 = [-1001154996282, 'https://t.me/joinchat/YQo7Tmn6vc9jN2Ji']
channel12 = [-1001401803824, 'https://t.me/joinchat/m0gU5IC1CqcwYTdi']



setka = [channel1,channel2,channel3,channel4,channel5,channel6,channel7,channel8,channel9,channel10,channel11,channel12]


list_word = ["<a href = '{}'>Загрузили слитые архивы в наш резерв</a>",
             "<a href = '{}'>🔑 Наш резерв</a>",
             "<a href = '{}'>⚜️ПPUвAT04Ka⚜️</a>",
             "<a href = '{}'>🔐Больше Zaпрещеного контента в нашем VIP🚫</a>",
             "<a href = '{}'>⚠️🍭VERY SECRET CONTENT👇🏻</a>",
             "<a href = '{}'>📌БОЛЕЕ 1260 ВИДЕО МОЛОДЫХ</a>",
             "<a href = '{}'>⁉️КАК ЕГО НЕ ЗАБЛОКИРОВАЛИ?🔞</a>"
             ]

async def time_now():
    await asyncio.sleep(5) #Ждем полной загрузки бота
    while True:
        offset = datetime.timezone(datetime.timedelta(hours=3))
        now_time = datetime.datetime.now(offset) #Текущая дата и время по МСК
        if int(now_time.hour) == 10:
            await postind_v_setku()
            await asyncio.sleep(3600)
        elif int(now_time.hour) == 19:
            await postind_v_setku()
            await asyncio.sleep(3600)

        await asyncio.sleep(60)




async def postind_v_setku():
    for i in range(1,len(setka)):
        r = random.randint(i, len(setka) - 1) #Выбираем рандомный номер канала
        a = await bot.copy_message(chat_id=setka[i-1][0],
                                   from_chat_id=channel_content,
                                   message_id=random.randint(start_count, count_posts),
                                   parse_mode='html',
                                   caption=(random.choice(list_word)).format(setka[r][1]))
        await asyncio.sleep(10)

    await bot.copy_message(chat_id=setka[-1][0],from_chat_id=channel_content,message_id=random.randint(start_count, count_posts))# Выкладывае пост в последний канал


async def new_cout_posts(new_coutn):
    global count_posts
    count_posts = new_coutn