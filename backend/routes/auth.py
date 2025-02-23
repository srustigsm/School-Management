from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

from backend.models.database import db

from flask_bcrypt import Bcrypt

auth = Blueprint('auth', __name__)
auth = Blueprint('auth', __name__)
bcrypt = Bcrypt()  # Initialize Bcrypt with the app context


# Initialize the database
db.init_app(auth)


@auth.route('/login', methods=['POST'])


@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']

    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    cursor.close()


    if user and bcrypt.check_password_hash(user['password'], password):
        session['user'] = user['email']
        session['role'] = user['role']
        
        access_token = create_access_token(identity=str(user['id']), additional_claims={"role": user['role']})
        return jsonify({'token': access_token, 'role': user['role']}), 200


    return jsonify({'message': 'Invalid credentials'}), 401
