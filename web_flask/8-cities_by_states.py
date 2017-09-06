#!/usr/bin/python3
"""
routes /cities_by_states
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def listCities():
    """display page listing all cities in a state"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """closes the current sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
