from flask import Blueprint,render_template,redirect,url_for
from my_project import db
from my_project.models import Owner
from my_project.owners.forms import AddForm

owner_blueprint = Blueprint('owners',__name__,template_folder='templates/owners')

@owner_blueprint.route('/add',methods=['GET','POST'])
def add_owner():
    form = AddForm()

    if form.validate_on_submit():
        id = form.id_puppy.data
        name = form.name.data
        new_owner = Owner(name,id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppies.list_pup'))

    return render_template('add_owner.html',form=form)