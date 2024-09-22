# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired

class PetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    type = SelectField('Type', choices=[('dog', 'Dog'), ('cat', 'Cat')], validators=[DataRequired()])
    submit = SubmitField('Add Pet')
