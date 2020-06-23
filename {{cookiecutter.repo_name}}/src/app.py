from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/goodbye/")
def goodbye():
    return "Goodbye World!"