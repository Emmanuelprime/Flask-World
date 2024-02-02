from flask import Flask,session,url_for,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from forms import AddForm,DelForm,AddOwner

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretekey'

#### set up database ########
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)

###############################

#Create Model

class Puppy(db.Model):
    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name
        
    def __repr__(self):
        if self.owner:
            return f"Puppy {self.name} has an owner whose name is {self.owner}"

        else:
            return f"Puppy {self.name} has no owner yet"


class Owner(db.Model):

    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    id_puppy = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,id_puppy):
        self.name = name
        self.id_puppy = id_puppy

    def __repr__(self):
        return f"Owner name is {self.name}"


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add',methods=['POST','GET'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)


@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@app.route('/delete',methods=['GET','POST'])
def delete_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        puppy = Puppy.query.get(id)
        db.session.delete(puppy)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('delete.html',form=form)

@app.route('/addowner',methods=['POST','GET'])
def add_owner():
    form = AddOwner()

    if form.validate_on_submit():
        id = form.id_puppy.data
        name = form.name.data
        new_owner = Owner(name,id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)