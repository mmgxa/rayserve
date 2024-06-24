from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="NOT A REAL KEY",
)
chat_completion = client.chat.completions.create(
    model="google/gemma-2b-it",
    messages=[
        {
            "role": "user",
            "content": "Please tell me a joke regarding Microsoft?'",
        },
    ],
    temperature=0.1,
    stream=True,
)

for chat in chat_completion:
    if chat.choices[0].delta.content is not None:
        print(chat.choices[0].delta.content, end="")
