#!/usr/bin/python3
"""
routes /states and /states/<id>
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', defaults={'id': 'empty'}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def listCities(id):
    """display page listing all cities in a state"""
    if id == "empty":
        allStates = storage.all('State').values()
        return render_template('9-states.html', states=allStates, sid=id)    
    else:
        allStates = storage.all('State').values()
        for st in allStates:
            if st.id == id:
                return render_template('9-states.html', states=allStates,
                                       sid=id, nme=st.name, city=st.cities)
    return render_template('9-states.html', sid=None)

@app.teardown_appcontext
def remove_session(exception=None):
    """closes the current sqlalchemy session"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
