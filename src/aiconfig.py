import openai

ENGINES = {
    'davinci-code': {
        'id': "code-davinci-002",
        'description': '''
Most capable Codex model. Particularly good at translating natural language to code. 
In addition to completing code, also supports inserting completions within code.
        '''
    },
    'cushman-code': {
        'id': "code-cushman-001",
        'description': '''
Almost as capable as Davinci Codex, but slightly faster. 
This speed advantage may make it preferable for real-time applications.
        '''
    },
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
