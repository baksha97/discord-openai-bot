import discord
from dotenv import dotenv_values
import openai

config = dotenv_values(".env")
OPEN_AI_TOKEN = config.get('OPEN_AI_TOKEN')
DISCORD_BOT_TOKEN = config.get('DISCORD_BOT_TOKEN')

ENGINES = {
    'davinci': {
        'id': "text-davinci-002",
        'description': '''
Davinci is the most capable engine and can perform any task the other models can perform and often with less instruction.
Good at: Complex intent, cause and effect, summarization for audience
        '''
    },
    'curie': {
        'id': "text-curie-001",
        'description': '''
Curie is extremely powerful, yet very fast. While Davinci is stronger when it comes to analyzing complicated text, Curie is quite capable for many nuanced tasks like sentiment classification and summarization. 
Curie is also quite good at answering questions and performing Q&A and as a general service chatbot.
Good at: Language translation, complex classification, text sentiment, summarization
        '''
    },
    'babbage': {
        'id': "text-babbage-001",
        'description': '''
Babbage can perform straightforward tasks like simple classification. It’s also quite capable when it comes to Semantic Search ranking how well documents match up with search queries.
Good at: Moderate classification, semantic search classification
        '''
    },
    'ada': {
        'id': "text-ada-001",
        'description': '''
Ada is usually the fastest model and can perform tasks like parsing text, address correction and certain kinds of classification tasks that don’t require too much nuance. Ada’s performance can often be improved by providing more context.
Good at: Parsing text, simple classification, address correction, keywords
        '''
    },
}

openai.api_key = OPEN_AI_TOKEN
bot = discord.Client()


def generate_response(
        prompt: str,
        engine: str,
        temperature: float = 0.8,
        max_tokens: int = 256
) -> str:
    response = openai.Completion.create(
        engine=ENGINES[engine]['id'],
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
    )
    return response.choices[0].text


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
