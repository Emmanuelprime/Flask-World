from my_project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



class User(db.Model,UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String,unique=True,index=True)
    pass_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.username = username
        self.pass_hash = generate_password_hash(password)
        self.email = email

    def check_password(self,password):
        return check_password_hash(self.pass_hash,password)
