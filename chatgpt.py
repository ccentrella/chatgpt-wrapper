import os
import sys
from openai import OpenAI

client = OpenAI()
try:
    with open('..instructions.txt', 'r') as file:
        instructions = file.read()
except FileNotFoundError:
    instructions = ''

prompt = " ".join(sys.argv[1:])
if prompt.strip() == '':
    raise AttributeError("Prompt is required")
model = os.environ.get('MODEL') or 'gpt-4o-mini'

print('\nWaiting for response from ChatGPT...')

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
