from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, InlineKeyboardMarkup
import weather
import token_for_bot

bot = Bot(token=token_for_bot.token_bot)
dp = Dispatcher(bot)


class Locale:
    Temp = "🌡️"
    START = "Hello! 👋 I'm a weather bot. For usage information, press /help."
    HELP = "Press the city name or send your location to get the weather."
    WEATHER_TEMPLATE = Temp + "The temperature in {} is {} °C."
    ERROR = "Oops! Something went wrong. Please try again."


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply(Locale.START)


@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message):
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [KeyboardButton("St.Petersburg 🏛️", callback_data="/spb")],
            [KeyboardButton("Moscow 🏙️", callback_data="/msk")],
            [KeyboardButton("Munich 🍺", callback_data="/muc")],
        ]
    )
    await message.reply(Locale.HELP, reply_markup=reply_markup)


@dp.callback_query_handler(text=["/spb", "/msk", "/muc"])
async def city_callback_handler(callback_query: types.CallbackQuery):
    city = callback_query.data[1:]
    try:
        location = weather.get_coordinates(city)
        temperature = weather.get_weather_from_location(
            location.latitude, location.longitude
        )
        weather_message = Locale.WEATHER_TEMPLATE.format(location.name, temperature)
        await callback_query.message.answer(weather_message)
    except Exception:
        await handle_error(callback_query.message.chat.id)


@dp.message_handler(content_types=["location"])
async def location_handler(message: types.Message):
    location = message.location
    try:
        temperature = weather.get_weather_from_location(
            location.latitude, location.longitude
        )
        _, street = weather.get_data_from_location(
            location.latitude, location.longitude
        )
        weather_message = Locale.WEATHER_TEMPLATE.format(street, temperature)
        await message.reply(weather_message)
    except Exception:
        await handle_error(message.chat.id)


async def handle_error(chat_id: int):
    await bot.send_message(chat_id, Locale.ERROR)


bot.polling()
