from groq import Groq
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def summarize_article(article):

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": article
            }
        ]
    )

    return json.loads(
        response.choices[0].message.content
    )