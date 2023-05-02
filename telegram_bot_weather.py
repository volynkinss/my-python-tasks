from aiogram import Bot, Dispatcher, executor, types
from weather import get_weather
import token_for_bot

bot = Bot(token=token_for_bot.token_bot)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello! I'm weather telegram bot and I can show actually weather for you. Enter '/spb' for see temperature in St.Petersburg, '/msk' for see temperature in Moscow and ‘/muc’ for see temperature in Munich")

@dp.message_handler(commands=['spb', 'msk', 'muc'])
async def weather_spb(message: types.Message):
    current_weather = get_weather(message.text[1:])
    await message.reply(f"Temperature in {current_weather[-1]} now is a {current_weather[0]['temperature']} degrees Celsius")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dp)
