#!/usr/bin/python3
"""
serves /, /hbnb and /c/<text>
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
@app.route('/c/<text>')
def cText(text):
    """displays text variable"""
    return "C {}".format(text.replace("_", " "))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
