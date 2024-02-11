import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)

#Enabling CORS for all routes
CORS(application)

# Random API key
API_KEY = 'ehtisham'


session_data = {}

application.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://hassan:pass@localhost/flasktask'

db=SQLAlchemy(application)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    grades = db.relationship('SubjectGrade', backref='user', lazy=True)


class SubjectGrade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(100))
    # You can encrypt the grade column here
    grade = db.Column(db.String(100))


# Home Page Route
@application.route('/', methods=['GET'])
def home():
    return "Home route"

# Get users information route
@application.route('/users', methods=['GET'])
def get_users_info():
    user_info = {
        'users': [
            {'name': 'Ehtisham', 'age': 18, 'gender': 'Male'},
            {'name': 'Ali', 'age': 19, 'gender': 'Male'},
            {'name': 'Iqbal', 'age': 25, 'gender': 'Male'},
            {'name': 'Usman', 'age': 28, 'gender': 'Male'},
            {'name': 'Amna', 'age': 40, 'gender': 'Female'}
        ]
    }
    return jsonify(user_info)


# Add users information route
@application.route('/add_usersinfo', methods=['POST'])
def add_users_information():
    try:
        if 'api_key' not in request.form or request.form['api_key'] != API_KEY:
            return jsonify({'error': 'Api key not matched.'}), 401

        user = User(
            name=request.form['name'],
            age=request.form['age'],
            gender=request.form['gender']
        )
        db.session.add(user)
        db.session.commit()

        # Return user ID
        return jsonify({'user_id': user.id}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Get Users Information Route
@application.route('/getusersinfo', methods=['POST'])
def get_users_information():
    try:
        if 'api_key' not in request.form or request.form['api_key'] != API_KEY:
            return jsonify({'error': 'API key not correct.'}), 401

        user_id = request.form.get('user_id')
        if not user_id:
            return jsonify({'error': 'User ID not provided.'}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({'error': 'User not found.'}), 404

        user_info = {
            'name': user.name,
            'age': user.age,
            'gender': user.gender
        }
        return jsonify({'user_info': user_info}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

if __name__ == "__main__":
    application.run(debug=True)
