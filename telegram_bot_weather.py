from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import weather
import token_for_bot


bot = Bot(token=token_for_bot.token_bot)
dp = Dispatcher(bot)
print("start of get_weather app")
base_of_msg_id = {}


def add_command_msg_id_to_list(
    message_id, chat_id
):  # function that add msg id of msg that call command to list_of_messages_id
    print(f"strat of add_command_msg_id_to_list_function for chat:{chat_id}")
    base_of_msg_id[chat_id].append(message_id)


def add_reply_msg_id_to_list(
    message_id, chat_id
):  # function that add msg id of msg replyed for command to list_of_messages_id
    print(f"strat of add_reply_msg_id_to_listfunction for chat:{chat_id}")
    base_of_msg_id[chat_id].append(message_id)


async def cleanup_chat_history(chat_id):  # function that delete unnecessary msgs
    print(f"strat of delete_msgs_function for chat:{chat_id}")
    while base_of_msg_id[chat_id] != []:
        for id in base_of_msg_id[chat_id]:
            await bot.delete_message(chat_id=chat_id, message_id=id)
            base_of_msg_id[chat_id].remove(id)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    chat_id = message.chat.id
    print(f"start function of comand 'start'for chat:{chat_id}")
    if chat_id not in base_of_msg_id:
        base_of_msg_id[chat_id] = []
    add_command_msg_id_to_list(message.message_id, chat_id)
    reply_message_id = message.message_id + 1
    add_reply_msg_id_to_list(reply_message_id, chat_id)
    print(base_of_msg_id)
    await message.reply(
        f"""Hello! 👋 I'm weather telegram bot and I can get actual weather for you.
For usage information press '/help'⬅️
"""
    )


button_spb = KeyboardButton("/spb")
button_msk = KeyboardButton("/msk")
button_muc = KeyboardButton("/muc")
button_location = KeyboardButton("location", request_location=True)
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_spb, button_msk, button_muc, button_location)

inline_button_spb = KeyboardButton("St.Petersburg 🏛️", callback_data="/spb")
inline_button_msk = KeyboardButton("Moscow 🏙️", callback_data="/msk")
inline_button_muc = KeyboardButton("Munich 🍺", callback_data="/muc")
inline_button_location = KeyboardButton("Location", request_location=True)
inline_greet_kb = InlineKeyboardMarkup(one_time_keyboard=True)
inline_greet_kb.add(inline_button_spb, inline_button_msk, inline_button_muc)


@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message):
    chat_id = message.chat.id
    print(f"start function of comand 'help' for chat:{chat_id}")
    add_command_msg_id_to_list(message.message_id, chat_id)
    reply_message_id = message.message_id + 1
    add_reply_msg_id_to_list(reply_message_id, chat_id)
    await message.reply(
        """Press:
'/spb' for see t° in St.Petersburg 🏛️, 
'/msk' for see t° in Moscow 🏙️ or 
'/muc' for see t° in Munich 🍺
or just send your current location to weather_bot 🙋‍♂️.
Let's start! 🚀""",
        reply_markup=inline_greet_kb,
    )


# @dp.callback_query_handler(filters.Text("/spb"))
# async def process_callback_inline_button_spb(callback_query: types.CallbackQuery):
#     await callback_query.message.answer("spb")


@dp.message_handler(commands=["spb", "msk", "muc"])
async def city_command_handler(message: types.Message):
    chat_id = message.chat.id
    print(f"start function of comand 'spb' or 'msk' or 'muc' for chat:{chat_id}")
    add_command_msg_id_to_list(message.message_id, chat_id)
    city = weather.get_coordinates(message.text)
    temperature = weather.get_weather_from_location(city.latitude, city.longitude)
    text = f"{city.name}'s t° now is a {temperature} °C"
    await message.reply(text)
    await cleanup_chat_history(chat_id)


@dp.message_handler(content_types=["location"])
async def location_handler(message: Message):
    chat_id = message.chat.id
    print(f"start function of get user location for chat:{chat_id}")
    add_command_msg_id_to_list(message.message_id, chat_id)
    location = message.location
    temperature = weather.get_weather_from_location(
        location.latitude, location.longitude
    )
    city, street = weather.get_data_from_location(location.latitude, location.longitude)
    text = f"Temperature in {city} near {street} in your location is {temperature} °C"
    await message.reply(text)
    await cleanup_chat_history(chat_id)


@dp.message_handler(content_types=["venue"])
async def venue_handler(message: Message):
    chat_id = message.chat.id
    print(f"start handle_message_function for chat:{chat_id}")
    add_command_msg_id_to_list(message.message_id, chat_id)
    location = message.location
    temperature = weather.get_weather_from_location(
        location.latitude, location.longitude
    )
    city, street = weather.get_data_from_location(location.latitude, location.longitude)
    text = f"Temperature in {city} near {street} in your location is {temperature} °C"
    await message.reply(text)
    await cleanup_chat_history(chat_id)


executor.start_polling(dp)
