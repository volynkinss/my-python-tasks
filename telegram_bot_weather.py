from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import weather
import token_for_bot


bot = Bot(token=token_for_bot.token_bot)
dp = Dispatcher(bot)


print("start of get_weather app")

list_of_messages_id = []


async def delete_msgs():  # function that delete unnecessary msgs
    print("strat of delete_msgs_function")
    while list_of_messages_id != []:
        for id in list_of_messages_id:
            await bot.delete_message(chat_id=218947055, message_id=id)
            list_of_messages_id.remove(id)


def add_command_msg_id_to_list(
    message: types.Message,
):  # function that add msg id of msg that call command to list_of_messages_id
    print("strat of add_command_msg_id_to_list_function")
    message_id = message.message_id
    list_of_messages_id.append(message_id)


def add_reply_msg_id_to_list(
    message: types.Message,
):  # function that add msg id of msg replyed for command to list_of_messages_id
    print("strat of add_reply_msg_id_to_listfunction")
    message_id = message.message_id + 1
    list_of_messages_id.append(message_id)


# @dp.message_handler(commands=["end"])
# async def get_messages_id(message: types.Message):
#     chat_id = 218947055
#     messages = await bot.get_messages(chat_id)
#     messages_id = [Message.message_id for message in messages]
#     # return messages_id
#     await message.reply(messages_id)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    add_command_msg_id_to_list(message)
    add_reply_msg_id_to_list(message)
    await message.reply(
        f"""Hello! 👋 I'm weather telegram bot and I can get actual weather for you.
For usage information press '/help'⬅️
"""
    )


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    add_command_msg_id_to_list(message)
    add_reply_msg_id_to_list(message)
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
    add_command_msg_id_to_list(message)
    city = weather.get_coordinates(message.text)
    temperature = weather.get_weather_from_location(city.latitude, city.longitude)
    text = f"{city.name}'s t° now is a {temperature} °C"
    await message.reply(text)
    await delete_msgs()


@dp.message_handler(content_types=["location"])
async def handle_location(message: Message):
    add_command_msg_id_to_list(message)
    location = message.location
    temperature = weather.get_weather_from_location(
        location.latitude, location.longitude
    )
    text = f"Temperature in your location now {temperature} °C"
    await message.reply(text)
    await delete_msgs()


# used functions below to test and learning


# @dp.message_handler(commands=["list"])
# async def list(message: types.Message):
#     message_id = message.message_id  # id of msg that call  this command
#     list_of_messages_id.append(message_id)
#     message_id = message.message_id + 1  # id of msg replyed for this command
#     list_of_messages_id.append(message_id)
#     await message.reply(
#         f"""list of messages_id: {list_of_messages_id}
# """
#     )


# @dp.message_handler(commands=["del"])
# async def delete(message: types.Message):
#     message_id = message.message_id  # id of msg that call  this command
#     list_of_messages_id.append(message_id)
#     await delete_msgs(list_of_messages_id)
#     await message.reply(
#         f"""list of messages_id: {list_of_messages_id} deleted
# """
#     )


executor.start_polling(dp)
