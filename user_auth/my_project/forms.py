from flask_wtf import FlaskForm

from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo

class Registration(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Name',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm','password must match!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def check_email(self,field):

        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Your email has being already registered")
    def check_username(self,field):

        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Your username is already taken ")
    

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')
    