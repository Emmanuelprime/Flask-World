from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretekey'

class InfoForm(FlaskForm):
    
    breed = StringField("what breed are you",validators=[DataRequired()])
    submit = SubmitField("submit")
        
        
@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"Your breed is {form.breed.data} ")
        # or flash(f"Your breed is {session['breed']} ")
    return render_template('index2.html',form=form)

    
if __name__ == '__main__':
    app.run(debug=True)