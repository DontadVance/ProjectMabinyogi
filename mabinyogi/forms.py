from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length

class CharacterForm(FlaskForm):
    char_name = StringField('Name', validators=[InputRequired()])
    char_race = SelectField('Race', validators=[DataRequired()])
    char_stature = SelectField('Stature', validators=[DataRequired()])
    char_class = SelectField('Class', validators=[DataRequired()])
