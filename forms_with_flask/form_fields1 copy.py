from flask import Flask,render_template,session,redirect,url_for,flash
from flask_wtf import FlaskForm
from wtforms import (StringField,SubmitField,
                     DateTimeField,RadioField,SelectField
                     ,TextAreaField,BooleanField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretekey'

class InfoForm(FlaskForm):
    
    breed = StringField("what breed are you",validators=[DataRequired()])
    neutered = BooleanField('Have You been Neutered?')
    mood = RadioField("Please Choose Your Mood",choices=[('mood_one','Happy'),('mood_two','Excited')])
    food = SelectField(u"pick your favorite food:",choices=[('chi','chicken'),
                                                            ('bf','beaf'),
                                                            ('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField("submit")
        
        
@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    
    if form.validate_on_submit():
        flash("You just submitted")
        #temporarily rememeber the user session
        # so we can parse this to a different endpoint
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food.data
        session['feedback'] = form.feedback.data
        
        #return redirect(url_for('thankyou'))
    return render_template('index1.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)