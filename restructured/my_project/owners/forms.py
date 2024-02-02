from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    id_puppy = IntegerField('id of puppy')
    name = StringField('Name of Owner')
    submit = SubmitField('add owner')
