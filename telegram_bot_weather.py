from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import weather
import token_for_bot


bot = Bot(token=token_for_bot.token_bot)
dp = Dispatcher(bot)

print("start of get_weather app")


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    await message.reply(
        """Hello! 👋 I'm weather telegram bot and I can get actual weather for you.
For usage information press '/help' ⬅️"""
    )


@dp.message_handler(commands=["help"])
async def welcome(message: types.Message):
    await message.reply(
        """Press:
'/spb' for see t° in St.Petersburg 🏛️, 
'/msk' for see t° in Moscow 🏙️ or 
'/muc' for see t° in Munich 🍺
or just send your current location to weather_bot 🙋‍♂️.
Let's start! 🚀"""
    )


@dp.message_handler(commands=["spb", "msk", "muc"])
async def handle_city_command(message: types.Message):
    city = weather.get_coordinates(message.text)
    temperature = weather.get_weather_from_location(
        city.latitude, city.longitude)
    text = f"{city.name}'s t° now is a {temperature} °C"
    await message.reply(text)


@dp.message_handler(content_types=["location"])
async def handle_location(message: Message):
    location = message.location
    temperature = weather.get_weather_from_location(
        location.latitude, location.longitude)
    text = f"Temperature in your location now {temperature} °C"
    await message.reply(text)


executor.start_polling(dp)
