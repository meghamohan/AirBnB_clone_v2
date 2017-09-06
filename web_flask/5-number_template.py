#!/usr/bin/python3
"""
serves /, /hbnb and /c/<text>
"""

from flask import Flask
from flask import render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display only if its a numbr"""
    if isinstance(n, int):
        return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def numberTemplate(n):
    """display html page only if its a num"""
    return render_template('5-number.html', num=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
