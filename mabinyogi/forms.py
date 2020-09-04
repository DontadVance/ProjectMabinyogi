from wtforms import Form, BooleanField, StringField, validators

class CharacterForm(Form):
    char_name = StringField('Name', validators=[validators.InputRequired()])
    char_race = SelectField('Race', validators=[validators.DataRequired()])
    char_stature = SelectField('Stature', validators=[validators.DataRequired()])
    char_class = SelectField('Class', validators=[validators.DataRequired()])
