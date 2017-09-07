#!/usr/bin/python3
"""
routes /states and /states/<id>
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', defaults={'id': 'all'}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def listCities(id):
    """display page listing all cities in a state"""
    states = storage.all("State").values()
    if id == 'all':
        return render_template('9-states.html', states=states)
    else:
        for state in states:
            if id == str(state.id):
                state1 = state
        return render_template('9-states.html', states=state1)

@app.teardown_appcontext
def remove_session(exception=None):
    """closes the current sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
