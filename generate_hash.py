from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "student"  # Replace this with the actual password
hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')

print("Hashed Password:", hashed_pw)
