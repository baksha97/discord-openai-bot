import discord
import openai
from dotenv import dotenv_values

from aiconfig import generate_response, AVAILABLE_ENGINES

config = dotenv_values(".env")
COMMAND_PREFIX = "!"
OPEN_AI_TOKEN = config.get('OPEN_AI_TOKEN')
DISCORD_BOT_TOKEN = config.get('DISCORD_BOT_TOKEN')

openai.api_key = OPEN_AI_TOKEN
bot = discord.Client()


@bot.event
async def on_ready():
    print("The bot is online!")


@bot.event
async def on_message(message):
    if message.content.startswith(f'{COMMAND_PREFIX}help'):
        message_reply = ''
        for engine in AVAILABLE_ENGINES:
            message_reply += f'`{COMMAND_PREFIX}{engine.name}`: {engine.description}\n'
        message_reply += f'Usage: `{COMMAND_PREFIX}<engine_name> <actual prompt>`.\n'
        message_reply += 'Costs: `davinci` > `curie` > `babbage` > `ada`.'
        await message.channel.send(message_reply)
        return

    for engine in AVAILABLE_ENGINES:
        if message.content.startswith(f'{COMMAND_PREFIX}{engine.name} '):
            prompt = message.content.replace(f'{COMMAND_PREFIX}{engine.name} ', '')
            message_reply = generate_response(prompt=prompt, engine=engine)
            await message.channel.send(message_reply)
            return


bot.run(DISCORD_BOT_TOKEN)
