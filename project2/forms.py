from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField('name of Puppy')
    submit = SubmitField('add puppy')


class DelForm(FlaskForm):
    id = IntegerField('Id of Puppy to remove')
    submit = SubmitField('remove puppy')


class AddOwner(FlaskForm):
    id_puppy = IntegerField('id of puppy')
    name = StringField('Name of Owner')
    submit = SubmitField('add owner')
