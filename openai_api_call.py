import openai
import os

api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key

grade_level = input("What grade level are your students?: ")
english_ability = input("What is the English ability?: ")
question_types = input("What exercise types are you interested in?: ")
vocab_bank = input("Type out their vocabulary list: ")

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    temperature = 0.5,
    max_tokens = 2000,
    messages = [
    {"role": "user", "content": f"Write multiple English Language exercises for students in grade {grade_level} with {english_ability} English ability. It should include exercises in the following formats: {question_types}. The vocab list is: {vocab_bank}"},
    {"role": "system", "content": "You are an English Language teacher that creates engaging English Language exercises for your students."}

]
    )

worksheet = open("english_exercises.txt", "w")
worksheet.write(f"\n{completion.choices[0].message.content}")
worksheet.close()


