from flask import Flask, jsonify

app=Flask(__name__)


#Home Page Route
@app.route('/',methods=['GET'])
def home():
    return "Home route"


#Get users information route
@app.route('/users',methods=['GET'])
def getusersinfo():
    user_info={
        'users': [
            {'name':'Ehtisham', 'age':18, 'gender':'Male'},
            {'name':'Ali', 'age':19, 'gender':'Male'},
            {'name':'Iqbal', 'age':25, 'gender':'Male'},
            {'name':'Usman', 'age':28, 'gender':'Male'},
            {'name':'Amna', 'age':40, 'gender':'Female'}
        ]
    }
    return jsonify(user_info)


if __name__=="__main__":
    app.run(debug=True)

