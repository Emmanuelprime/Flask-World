from flask import Flask,render_template,redirect,url_for,flash,abort,request
from my_project import db, app
from flask_login import login_user,login_required,logout_user
from my_project.forms import LoginForm, Registration
from my_project.models import User


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcom.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out")
    return redirect(url_for('home'))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        print(user)
        if user is not None and user.check_password(password):
            login_user(user)
            flash('login successful')
            next = request.args.get('next') # saves what the user wanted to do that requiers login
            if next==None or not next[0] =='/':
                next = url_for('welcome_user')
            
            return redirect(next)

    return render_template('login.html',form=form)

@app.route('/register',methods=['GET', 'POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = User(email=email,username=username,password=password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful')

        return redirect(url_for('login'))

    return render_template('register.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)



