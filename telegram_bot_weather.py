from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import weather
import token_for_bot


bot = Bot(token=token_for_bot.token_bot)
dp = Dispatcher(bot)
print("start of get_weather app")
base_of_data_chats = {}


def add_command_msg_id_to_list(
    message: types.Message, chat_id
):  # function that add msg id of msg that call command to list_of_messages_id
    print(f"strat of add_command_msg_id_to_list_function for chat:{chat_id}")
    message_id = message.message_id
    base_of_data_chats[chat_id].append(message_id)
    print(base_of_data_chats[chat_id])


def add_reply_msg_id_to_list(
    message: types.Message, chat_id
):  # function that add msg id of msg replyed for command to list_of_messages_id
    print(f"strat of add_reply_msg_id_to_listfunction for chat:{chat_id}")
    message_id = message.message_id + 1
    base_of_data_chats[chat_id].append(message_id)
    print(base_of_data_chats[chat_id])


async def delete_msgs(chat_id):  # function that delete unnecessary msgs
    print(f"strat of delete_msgs_function for chat:{chat_id}")
    while base_of_data_chats[chat_id] != []:
        for id in base_of_data_chats[chat_id]:
            print(f"from {chat_id} deleted {id}")
            await bot.delete_message(chat_id=chat_id, message_id=id)
            base_of_data_chats[chat_id].remove(id)


@dp.message_handler(commands=["start"])
async def welcome(message: types.Message):
    chat_id = message.chat.id
    print(f"start function of comand 'start'for chat:{chat_id}")
    if chat_id in base_of_data_chats:
        pass
    else:
        base_of_data_chats[chat_id] = []
    add_command_msg_id_to_list(message, chat_id)
    add_reply_msg_id_to_list(message, chat_id)
    print(base_of_data_chats)
    await message.reply(
        f"""Hello! 👋 I'm weather telegram bot and I can get actual weather for you.
For usage information press '/help'⬅️
"""
    )


# @dp.message_handler(commands=["end"])
# async def get_messages_id(message: types.Message):
#     chat_id = 218947055
#     messages = await bot.get_messages(chat_id)
#     messages_id = [Message.message_id for message in messages]
#     # return messages_id
#     await message.reply(messages_id)


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    chat_id = message.chat.id
    print(f"start function of comand 'help' for chat:{chat_id}")
    add_command_msg_id_to_list(message, chat_id)
    add_reply_msg_id_to_list(message, chat_id)
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
    chat_id = message.chat.id
    print(f"start function of comand 'spb' or 'msk' or 'muc' for chat:{chat_id}")
    add_command_msg_id_to_list(message, chat_id)
    city = weather.get_coordinates(message.text)
    temperature = weather.get_weather_from_location(city.latitude, city.longitude)
    text = f"{city.name}'s t° now is a {temperature} °C"
    await message.reply(text)
    await delete_msgs(chat_id)


@dp.message_handler(content_types=["location"])
async def handle_location(message: Message):
    chat_id = message.chat.id
    print(f"start function of get user location for chat:{chat_id}")
    add_command_msg_id_to_list(message, chat_id)
    location = message.location
    temperature = weather.get_weather_from_location(
        location.latitude, location.longitude
    )
    text = f"Temperature in your location now {temperature} °C"
    await message.reply(text)
    await delete_msgs(chat_id)


# used functions below to test and learning


# @dp.message_handler(commands=["list"])
# async def list(message: types.Message):
#     chat_id = message.chat.id
#     print(f"start function of comand 'list' for chat:{chat_id}")
#     # message_id = message.message_id  # id of msg that call  this command
#     # list_of_messages_id.append(message_id)
#     # message_id = message.message_id + 1  # id of msg replyed for this command
#     # list_of_messages_id.append(message_id)
#     await message.reply(
#         f"""list of messages_id: {base_of_data_chats[chat_id]}
# """
#     )


# @dp.message_handler(commands=["del"])
# async def delete(message: types.Message):
#     chat_id = message.chat.id
#     await delete_msgs(chat_id)
#     await message.reply(
#         f"""list of messages_id: {list_of_messages_id} deleted
# """
#     )


executor.start_polling(dp)
