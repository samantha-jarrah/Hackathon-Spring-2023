from flask import render_template, flash, redirect, request
from app import app
from app.forms import AppForm
from app.pdf_generator import PDF
import openai
import os


api_key = os.environ.get("OPENAI_API_KEY")
openai.api_key = api_key


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Emily'}
    alist = [1, 2]
    return render_template('index.html', title='Hackathon 2023', user=user, alist=alist)


@app.route('/getform', methods=['GET', 'POST'])
def getform():
    form = AppForm()

    if form.validate_on_submit():
        grade_level = form.grade_level.data
        english_ability = form.english_ability.data
        question_types = form.get_question_types()
        vocabulary = form.vocabulary_words.data

        # Make an API call to OpenAI using the form inputs
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.8,
            max_tokens=2000,
            messages=[
                {"role": "user", "content": f"Write English Language exercises for students in the {grade_level} with {english_ability} English ability. It should include exercises in the following formats: {question_types}. The vocab list is: {vocabulary}. Please include a word bank of the vocabulary words before each set of questions. Also, please randomize the order that the vocabulary answers appear in the activity and only include one set of questions per question format type."},
                {"role": "system", "content": "You are an English Language teacher that creates engaging English Language exercises for your students."}
            ]
        )

        ai_response = f"\n{completion.choices[0].message.content}"

        pdf = PDF()
        pdf.set_title('Vocabulary Worksheet')
        pdf.add_page()
        pdf.chapter_body(ai_response)
        pdf.generate_pdf(ai_response)

        return render_template('output_page.html', output=ai_response)

        # flash('Vocabulary exercises generated successfully!', 'success')
        # return redirect('/index')

    return render_template('getform.html', title='Get Form', form=form)