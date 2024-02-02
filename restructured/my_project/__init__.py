import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretekey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app,db)

#register the blueprints

from my_project.puppies.views import puppies_blueprint
from my_project.owners.views import owner_blueprint

app.register_blueprint(owner_blueprint,url_prefix='/owners')
app.register_blueprint(puppies_blueprint,url_prefix='/puppies')
