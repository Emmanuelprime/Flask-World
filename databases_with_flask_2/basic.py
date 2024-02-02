from  models import db,Puppy,Owner,Toy

rufus = Puppy('Rufus')
fido = Puppy('Fido')

db.session.add_all([rufus,fido])
db.session.commit()

print(Puppy.query.all())

#grab rufus

rufus = Puppy.query.filter_by(name='Rufus').first() # first puppy named Rufus

#create owner
prime = Owner('Jose',rufus.id)
#give rufus some toys

toy1 = Toy('Chew Toy',rufus.id)
toy2 = Toy('Ball',rufus.id)
db.session.add_all([prime,toy1,toy2])
db.session.commit()

#grab rus again
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

print(rufus.report_toys())
