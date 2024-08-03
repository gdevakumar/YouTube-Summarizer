from groq import Groq
from openai import OpenAI
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()


def get_gpt_response(context, prompt):
    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
            {"role": "system", "content": f"{prompt}"},
            {"role": "user", "content": f"{context}"}
        ]
    )
    return completion.choices[0].message.content


def get_claude_response(context, prompt):
    client = Anthropic()
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=8000,
        messages=[
                {"role": "system", "content": f"{prompt}"},
                {"role": "user", "content": f"{context}"}
            ]
        )
    return message.content


def get_llama_response(context, prompt):
    client = Groq()
    chat_completion = client.chat.completions.create(
        model="llama-3.1-405b-reasoning",
        messages=[
                {"role": "system", "content": f"{prompt}"},
                {"role": "user", "content": f"{context}"}
            ]
    )
    return chat_completion.choices[0].message.content
