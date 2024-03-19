from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.venv/.env')

def generateChatResponse(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]

    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    model = "gpt-3.5-turbo"

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.5 
        )
        
        answer = response.choices[0].message.content.replace('\n', '<br>')
    except Exception as e:
        print("Error: ", e)
        answer = "error"

    return {'answer': answer}


