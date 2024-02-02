from flask import Blueprint,render_template,redirect,url_for
from my_project import db
from my_project.models import Puppy
from my_project.puppies.forms import AddForm,DelForm

puppies_blueprint = Blueprint('puppies',__name__,template_folder='templates/puppies')

@puppies_blueprint.route('/add',methods=['GET','POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))

    return render_template('add.html',form=form)

@puppies_blueprint.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@puppies_blueprint.route('/delete',methods=['GET','POST'])
def delete_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        puppy = Puppy.query.get(id)
        db.session.delete(puppy)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))

    return render_template('delete.html',form=form)