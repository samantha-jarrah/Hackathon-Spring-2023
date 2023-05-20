from flask import render_template, flash, redirect, request
from app import app
from app.forms import AppForm
import openai


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
        # TODO: Implement the logic to generate the vocabulary exercises using the OpenAI API

        flash('Vocabulary exercises generated successfully!', 'success')
        return redirect('/index')

    return render_template('getform.html', title='Get Form', form=form)
