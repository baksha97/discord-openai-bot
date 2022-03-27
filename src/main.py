import discord
from discord.ext import commands
from dotenv import dotenv_values
import openai

config = dotenv_values(".env")
OPEN_AI_TOKEN = config.get('OPEN_AI_TOKEN')
DISCORD_BOT_TOKEN = config.get('DISCORD_BOT_TOKEN')

openai.api_key = OPEN_AI_TOKEN
bot = commands.Bot(command_prefix='>')


def generate_response(prompt: str) -> str:
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.9,
        max_tokens=120
    )
    print(response)
    return response.choices[0].text

@bot.event
async def on_message(message):
    if message.content.startswith('$p'):
        content = message.content.replace('$p ', "")
        message_reply = generate_response(content)
        await message.channel.send(message_reply)

bot.run(DISCORD_BOT_TOKEN)
