import os
import sys
from openai import OpenAI

def send_request():
    instructions, model, prompt = load_information()
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": instructions
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(completion.choices[0].message.content)

def load_information():
    try:
        with open('..instructions.txt', 'r') as file:
            instructions = file.read()
    except FileNotFoundError:
        instructions = ''

    model = os.environ.get('MODEL') or 'gpt-4o-mini'
    prompt = " ".join(sys.argv[1:])
    if prompt.strip() == '':
        raise AttributeError("Prompt is required")

    print('\nWaiting for response from ChatGPT...')

    return instructions, model, prompt

send_request()
