#!/usr/bin/python3
"""
simple flask app
why use strictslash false :https://stackoverflow.com/questions/17285826/
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def helloHbnb():
    """displays hello HBNB"""
    return "Hello HBNB!"
@app.route('/hbnb')
def HBNB():
    """Displays HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
