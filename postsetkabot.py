from aiogram import executor
from misc import dp
import asyncio
import handlers
from handlers.sqlit import startbot
from handlers.worktime import time_now



if __name__ == "__main__":
    startbot() #Создание стартовых необходимых таблиц в боте
    loop = asyncio.get_event_loop()
    loop.create_task(time_now())
    executor.start_polling(dp, skip_updates=True)