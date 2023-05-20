from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AppForm(FlaskForm):
    multiple_choice = BooleanField('Multiple Choice')
    fill_in_the_blank = BooleanField('Fill in the Blank')
    definition_matching = BooleanField('Definition Matching')
    synonym = BooleanField('Synonym')
    antonym = BooleanField('Antonym')
    fill_in_the_letters = BooleanField('Fill in the Letters Spelling')
    submit = SubmitField('Get WorkSheet')
    vocabulary_words = StringField(
        'Vocabulary List', validators=[DataRequired()])
    grade_level = SelectField('Grade Level', choices=[
        ('1', '1st Grade'),
        ('2', '2nd Grade'),
        ('3', '3rd Grade'),
        ('4', '4th Grade'),
        ('5', '5th Grade'),
        ('6', '6th Grade')
    ])
    english_ability = SelectField('English Ability', choices=[(
        '1', 'Beginner'), ('2', 'Intermediate'), ('3', 'Advanced')])
    remember_me = BooleanField('Remember Me')

    def get_question_types(self):
        question_types = []
        if self.fill_in_the_blank.data:
            question_types.append('Fill in the Blank')
        if self.definition_matching.data:
            question_types.append('Definition Matching')
        if self.multiple_choice.data:
            question_types.append('Multiple Choice')
        if self.synonym.data:
            question_types.append('Synonym')
        if self.antonym.data:
            question_types.append('Antonym')
        return question_types
