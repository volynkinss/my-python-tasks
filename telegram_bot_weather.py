from aiogram import Bot, Dispatcher, executor, types
from weather import get_weather_from_location, get_coordinates
import token_for_bot
from aiogram.types import Message, Location

bot = Bot(token=token_for_bot.token_bot)
dp = Dispatcher(bot)

print("start of get_weather app")


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.reply(
        """Hello!👋 I'm weather telegram bot and I can show actually weather for you.
For read usage information press '/help'⬅️"""
    )


@dp.message_handler(commands=["help"])
async def welcome(message: types.Message):
    await message.reply(
        """Press:
'/spb' for see temperature in St.Petersburg🏛️, 
'/msk' for see temperature in Moscow🏙️ or 
'/muc' for see temperature in Munich🍺. 
If you want to get temperature in your location you should to send your location to weather_bot🙋‍♂️.
Let's started!🚀"""
    )


@dp.message_handler(commands=["spb", "msk", "muc"])
async def weather(message: types.Message):
    location, geolocation = get_coordinates(message.text[1:])
    temperature = get_weather_from_location(location)
    text = f"Temperature in {geolocation} now is a {temperature} degrees Celsius"
    await message.reply(text)


@dp.message_handler(content_types=["location"])
async def handle_location(message: Message):
    location = message.location
    temperature = get_weather_from_location(location)
    text = f"Temperature in your location now is a {temperature} degrees Celsius"
    await message.reply(text)


executor.start_polling(dp)
