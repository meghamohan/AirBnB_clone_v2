#!/usr/bin/python3
"""
combining sqlalchemy with flask
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list/', strict_slashes=False)
def displayStatesList():
    """ list all states"""
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def closeSession(exception=None):
    """close the current sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
