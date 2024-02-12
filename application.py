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
    grade = db.Column(db.String(100))


# encrypted_grade = db.Column(db.LargeBinary)

#     def _init_(self, **kwargs):
#         super(SubjectGrade, self)._init_(**kwargs)
#         self._cipher_suite = Fernet(Fernet.generate_key())


#     @property
#     def grade(self):
#         return self._decrypt_grade()

#     @grade.setter
#     def grade(self, value):
#         self.encrypted_grade = self._encrypt_grade(value)

#     def _encrypt_grade(self, grade):
#         return self._cipher_suite.encrypt(grade.encode())

#     def _decrypt_grade(self):
#         if self.encrypted_grade:
#             return self._cipher_suite.decrypt(self.encrypted_grade).decode()
#         return None

   
# # Set up event listeners to automatically encrypt and decrypt the grade
# @event.listens_for(SubjectGrade, 'before_insert')
# def before_insert(mapper, connection, target):
#     if target.grade:
#         target._encrypted_grade = target._encrypt_grade(target.grade)


# @event.listens_for(SubjectGrade, 'before_update')
# def before_update(mapper, connection, target):
#     if target.grade:
#         target._encrypted_grade = target._encrypt_grade(target.grade)


# @event.listens_for(SubjectGrade, 'load')
# def on_load(target, context):
#     if target._encrypted_grade:
#         target.grade = target._decrypt_grade()

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
    

# Add Users Grade
@application.route("/addusersgrade",methods=['POST'])
def addusersgrade():
    try:
        if 'api_key' not in request.form:
            return jsonify({'error': 'API key not passed by the user.'}),401
        
        if request.form['api_key']!=API_KEY:
            return jsonify({'error':'API key not matched.'}),401
        
        # Extract form data
        user_id = request.form.get('user_id')
        subject = request.form.get('subject')
        grade = request.form.get('grade')

        # Check if any required field is missing
        if not user_id or not subject or not grade:
            return jsonify({'error': 'Some entries are missing.'}), 400


        grades= SubjectGrade(
            user_id= user_id,
            subject= subject,
            grade =grade
        )


        db.session.add(grades)
        db.session.commit()

        # Return user id
        return jsonify({'grade_id': grades.id}),200
    
    except Exception as e:
        return jsonify({'Error: ':str(e)}),400
    

# Get User Grades Information on the basis of user id.
@application.route('/getusergrades', methods=['POST'])
def getgrades():
    try:
        if 'api_key' not in request.form:
            return jsonify({"Error:": 'API_Key not Provided.'}), 401
        
        if request.form['api_key'] != API_KEY:
            return jsonify({"Error:": "API Key not matched."}), 401
        
        user_id = request.form.get('user_id')
        if not user_id:
            return jsonify({'Error:': 'User Id not provided.'}), 400
        
        # Fetch all grades for the specified user_id
        grades = SubjectGrade.query.filter_by(user_id=user_id).all()
        
        if not grades:
            return jsonify({'Error:': 'No grades found for the specified user.'}), 404
        
        # Created a list to store grade information for each entry
        grade_information = []
        for grade in grades:
            grade_info = {
                'user_id': grade.user_id,
                'subject': grade.subject,
                'grade': grade.grade
            }
            grade_information.append(grade_info)

        return jsonify({'Grades:': grade_information}), 200
    
    except Exception as e:
        return jsonify({"Error": str(e)}), 500



if __name__ == "__main__":
    application.run(debug=True)