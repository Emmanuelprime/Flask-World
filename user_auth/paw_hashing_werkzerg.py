from werkzeug.security import generate_password_hash,check_password_hash



password = 'mypassword'
hased = generate_password_hash(password)
print(hased)

check = check_password_hash(hased,'mu')

print(check)