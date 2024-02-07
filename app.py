import uuid
from flask import Flask, jsonify, request

app = Flask(__name__)

# Random API key
API_KEY = 'ehtisham'

# Home Page Route
@app.route('/', methods=['GET'])
def home():
    return "Home route"

# Get users information route
@app.route('/users', methods=['GET'])
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
@app.route('/add_usersinfo', methods=['POST'])
def add_users_information():
    try:
        if 'api_key' not in request.form or request.form['api_key'] != API_KEY:
            return jsonify({'error': 'Api key not matched.'}), 401

        # Generating the session id for the user
        session_id = str(uuid.uuid4())

        user_info = {
            'name': request.form['name'],
            'age': request.form['age'],
            'gender': request.form['gender']
        }

        session_data = {}

        session_data[session_id] = user_info

        # Return session ID
        return jsonify({'session_id': session_id}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

#Get Users Information Route
@app.route('/getusersinfo', methods=['POST'])
def getusersinformation():
    try:

        
        session_data={}
        
        if 'api_key' not in request.form:
            return({'error':'API key not found.'}),400
        
        if 'session_id' not in request.form:
            return({'error':'Session Id not found.'}),400
        
        if request.form['api_key']!=API_KEY:
            return({'error':'API key not correct.'}),401
        
        session_id=request.form['session_id']

        
        if session_id not in session_data:
            return jsonify({'error': 'Session ID not found.'}), 401
        

        # Get user information associated with the session ID
        user_info = session_data[session_id]

        # Return the user information
        return jsonify({'user_info': user_info}), 200

        
    except Exception as e:
        return jsonify({'error':'Exception in this route'}),500


if __name__ == "__main__":
    app.run(debug=True)
