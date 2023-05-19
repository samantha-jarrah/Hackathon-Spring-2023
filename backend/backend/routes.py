from flask import render_template
from backend import backend
from backend.forms import AppForm

@backend.route('/')
@backend.route('/index')
def index():
    user = {'username': 'Emily'}
    alist = [1, 2]
    return render_template('index.html', title='Hackathon 2023', user=user, alist=alist)

@backend.route('/getform')
def getform():
    form = AppForm()
    return render_template('getform.html', title='Get Form', form=form)