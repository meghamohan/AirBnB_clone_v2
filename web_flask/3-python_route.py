#!/usr/bin/python3
"""
serves /, /hbnb and /c/<text>
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHbnb():
    """displays hello HBNB"""
    return "Hello HBNB!"
@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Displays HBNB"""
    return "HBNB"
@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """displays text variable"""
    txt = text.replace('_', ' ')
    return "C {}".format(txt)
@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def pythonText(text="is cool"):
    """displays python is cool"""
    txt = " ".join(text.split('_'))
    return "Python {}".format(txt)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
