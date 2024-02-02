import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base_dir = os.path.abspath(os.path.dirname(__file__)) #directoty to store the db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # we dont want to track every single modification

db = SQLAlchemy(app)

migrate = Migrate(app,db) # adding migration caps


class Puppy(db.Model):
    __tablename__ = 'puppies' 
    
    #create the columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.text)
    
    def __init__(self, name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"