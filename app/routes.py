from flask import render_template, flash, redirect
from app import app
from app.forms import AppForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Emily'}
    alist = [1, 2]
    return render_template('index.html', title='Hackathon 2023', user=user, alist=alist)

@app.route('/getform', methods=['GET', 'POST'])
def getform():
    form = AppForm()
     
    return render_template('getform.html', title='Get Form', form=form)