from my_project import db

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
