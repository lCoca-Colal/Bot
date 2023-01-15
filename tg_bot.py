import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token, user_id
from main import check_films_update


bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp =  Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ['Все фильмы', 'Последние 5 фильмов', 'Свежие фильмы']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    
    await message.answer("Лента", reply_markup=keyboard)
    
    
@dp.message_handler(Text(equals="Все фильмы"))
async def get_all_films(message: types.Message):
    with open('film_dict.json') as file:
        film_dict = json.load(file)
     
      
     
    for k, v in sorted(film_dict.items()):
        films = f"<b>{v['articles_title']}</b>\n" \
                f"{v['articles_url']}"

        await message.answer(films)
        
@dp.message_handler(Text(equals="Последние 5 фильмов"))
async def get_last_five_films(message: types.Message):
    with open('film_dict.json') as file:
        film_dict = json.load(file)
        
    for k, v in sorted(film_dict.items())[-5:]:
        films = f"<b>{v['articles_title']}</b>\n" \
                f"{v['articles_url']}"

        await message.answer(films)
        
@dp.message_handler(Text(equals="Свежие фильмы"))
async def get_fresh_films(message: types.Message):
    fresh_films = check_films_update()
    
    if len(fresh_films) >= 1:
        for k, v in sorted(fresh_films.items()):
            films = f"<b>{v['articles_title']}</b>\n" \
                    f"{v['articles_url']}"

            await message.answer(films)
    else:
        await message.answer('Нет свежих новостей')
        
        
# async def films_every_day():
#     while True:
#         fresh_films = check_films_update()
    
#         if len(fresh_films) >= 1:
#             for k, v in sorted(fresh_films.items()):
#                 films = f"<b>{v['articles_title']}</b>\n" \
#                         f"{v['articles_url']}"

#                 await bot.send_message(user_id, films, disable_notification=True)
#         else:
#             await bot.send_message(user_id, 'Пока нет свежих фильмов...', disable_notification=True)
        
           
            
if __name__ == '__main__': 
    executor.start_polling(dp)