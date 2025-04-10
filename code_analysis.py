import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def roast_code_file(code_text):
    prompt = f"You're a sarcastic AI named Wednesday. Roast this Python code line by line:\n{code_text}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content[:2000]
