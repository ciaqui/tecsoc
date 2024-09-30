from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Regexp, InputRequired, NumberRange, Email

class ExampleForm(FlaskForm):
    example_field = StringField('Example Field *', validators=[DataRequired()])
    submit = SubmitField('Submit')