import openai

openai.api_key = ""

completionHistory = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 1.0,
    max_tokens = 2000,
    messages = [
    {"role": "user", "content": f"Write {num} multiple choice US history questions, for children {age} years old."}
]
    )

{completionHistory.choices[0].message.content}

