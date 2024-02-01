from basic import db,Puppy


#Create all the table
db.create_all()

#create new entries

sam = Puppy('Sammy',3)
frank = Puppy('frank',4)

db.session.add_all([sam,frank]) # adds the new entries to the db
# or db.session.add(sam)
db.session.commit() # saves the data


print(sam.id)
print(frank.id)
