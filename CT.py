from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

'''
@app.route('/convlen')
def convlen():
    return render_template("lenconv.html")

@app.route('/convweight')
def convweight():
    return render_template("weightconv.html")
'''
@app.route('/index')
def index():
    return render_template("buttons.html")

if __name__== "__main__":
	app.run(debug=True)