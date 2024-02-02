from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'mypassword'
hased = bcrypt.generate_password_hash(password)
print(hased)

check = bcrypt.check_password_hash(hased,'mypassword')

print(check)