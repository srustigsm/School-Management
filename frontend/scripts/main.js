from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, JWTManager

auth = Blueprint('auth', __name__)

# Dummy user authentication data
users = {
    "john@school.com": {"password": "hashed_password", "role": "headmaster"},
    "jane@school.com": {"password": "teacher", "role": "teacher"},
    "michael@school.com": {"password": "parent", "role": "parent"},
}

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')  # Correct key retrieval
    password = data.get('password')  # Correct key retrieval

    # Validate user
    if email in users and users[email]["password"] == password:
        # Generate JWT Token
        token = create_access_token(identity=email, additional_claims={"role": users[email]["role"]})

        return jsonify({
            "message": "Login successful",
            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MDMxNjY5MywianRpIjoiZjVmZmRjZTgtOWMwNy00YjA0LThhZmItODljZjgzZGJkN2U1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjEiLCJuYmYiOjE3NDAzMTY2OTMsImNzcmYiOiIyOWZkM2E4MS03YTIyLTRjMGItYWIzMS1jYjZhMDJkODNhY2YiLCJleHAiOjE3NDAzMTc1OTMsInJvbGUiOiJoZWFkbWFzdGVyIn0.gnNNMqlWycCmhkGu_V7E-ji8jEykV8nUdks0KBKjhoY",  # Corrected token format
            "role": users[email]['role']  # Corrected role retrieval
        }), 200

    return jsonify({"message": "Invalid credentials"}), 401
