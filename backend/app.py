from flask import Flask, render_template, request, jsonify
import mysql.connector
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
import os

app = Flask(__name__)

# ✅ Use environment variables for sensitive data
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'Nive@2005')
jwt = JWTManager(app)

bcrypt = Bcrypt(app)

# ✅ Create a function to get a new database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nive@203005",
        database="classconnect"
    )

# ✅ Serve Login Page
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Serve Dashboards
@app.route('/headmaster')
def headmaster():
    return render_template('headmaster.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

@app.route('/parent')
def parent():
    return render_template('parent.html')

# ✅ Test Database Connection
@app.route('/test_db', methods=['GET'])
def test_db():
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT 1")
        cursor.close()
        db.close()
        return jsonify({"message": "Database connection is working!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ User Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Email and password are required'}), 400

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
        cursor.close()
        db.close()

        if not user:
            return jsonify({'message': 'User not found'}), 404

        if bcrypt.check_password_hash(user['password'], password):
            access_token = create_access_token(identity=str(user['id']), additional_claims={"role": user['role']})
            return jsonify({'token': access_token, 'role': user['role']}), 200

        return jsonify({'message': 'Invalid credentials'}), 401

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ API to Get Student Data (Only Parents Can Access)
@app.route('/students', methods=['GET'])
@jwt_required()
def get_students():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return jsonify(students)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        db.close()

# ✅ Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
