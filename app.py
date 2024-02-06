from flask import Flask

app=Flask(__name__)


#Home Page Route
@app.route('/',methods=['GET'])
def home():
    return "Home route"


if __name__=="__main__":
    app.run(debug=True)

