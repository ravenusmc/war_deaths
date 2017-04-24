from flask_wtf import Form
from wtfforms import IntegerField, SubmitField

class SignupForm(Form):
    number = IntegerField('number')
    submit = SubmitField('Enter')
