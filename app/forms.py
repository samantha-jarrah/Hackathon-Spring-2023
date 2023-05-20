from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class AppForm(FlaskForm):
    #multiple_choice = BooleanField('Multiple Choice')
    fill_in_the_blank = BooleanField('Fill in the Blank')
    definition_matching = BooleanField('Definition Matching')
    synonym = BooleanField('Synonym')
    antonym = BooleanField('Antonym')
    fill_in_the_letters = BooleanField('Fill in the Letters Spelling')
    submit = SubmitField('Get WorkSheet')
    vocabulary_words = StringField('Vocabulary Words', validators=[DataRequired()])
    #grade_level = SelectField('Select Grade Level', choices=[('1', 'Grade Level 1') ('2', 'Grade Level 2'), ('3', 'Grade Level 3'), ('4', 'Grade Level 4'), ('5', 'Grade Level 5')])
    english_ability = SelectField('Select English Ability', choices=[('1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced')])
    remember_me = BooleanField('Remember Me')