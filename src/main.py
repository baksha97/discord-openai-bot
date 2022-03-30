import discord
import openai
from dotenv import dotenv_values

from aiconfig import generate_response, ENGINES

config = dotenv_values(".env")
OPEN_AI_TOKEN = config.get('OPEN_AI_TOKEN')
DISCORD_BOT_TOKEN = config.get('DISCORD_BOT_TOKEN')

openai.api_key = OPEN_AI_TOKEN
bot = discord.Client()


@bot.event
async def on_ready():
    print("The bot is online!")


@bot.event
async def on_message(message):
    if message.content.startswith('$help'):
        message_reply = ''
        for engine_name in ENGINES.keys():
            message_reply += f'`${engine_name}`: {ENGINES[engine_name]["description"]}\n'
        message_reply += 'Usage: `$<engine_name> <actual prompt>`.\n'
        message_reply += 'Costs: `davinci` > `curie` > `babbage` > `ada`.'
        await message.channel.send(message_reply)
        return

    for engine_name in ENGINES.keys():
        if message.content.startswith(f'${engine_name} '):
            prompt = message.content.replace(f'${engine_name} ', '')
            message_reply = generate_response(prompt=prompt, engine=engine_name)
            await message.channel.send(message_reply)
            return


bot.run(DISCORD_BOT_TOKEN)
