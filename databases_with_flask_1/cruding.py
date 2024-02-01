from basic import db,Puppy

#Create

# prime = Puppy("Prime",5)
# db.session.add(prime)
# db.session.commit()

#READ

# all_pup = Puppy.query.all() #returns a list of puppies in the table
# print(all_pup)

#query by id
# first_pup = Puppy.query.get(1)
# print(first_pup)

#filter

# all_prime = Puppy.query.filter_by(name='Prime')
# print(all_prime.all())

#UPDATE

# first_puppy = Puppy.query.get(1)
# first_puppy.age = 10
# db.session.add(first_puppy)
# db.session.commit()

#DELETING

prime = Puppy.query.get(5)
db.session.delete(prime)
db.session.commit()