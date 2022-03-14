from flask import Flask
from 8puzzle import run
app = Flask(__name__)

@app.route("/")
def hello_world():
    run()
    return "<p>Hello, World!</p>"

hello_world()