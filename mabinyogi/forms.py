from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length

class CharacterForm(FlaskForm):
    char_name = StringField('Name', validators=[InputRequired()])
    char_race = SelectField('Race', validators=[DataRequired()], choices=[('Human'),('Orc'),('Elf')])
    char_stature = SelectField('Stature', validators=[DataRequired()], choices=[('Feminine'),('Masculine')])
    char_class = SelectField('Class', validators=[DataRequired()], choices=[('Warrior'),('Rogue'),('Mage')])
