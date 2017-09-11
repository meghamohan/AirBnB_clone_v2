#!/usr/bin/python3
"""
routes /states and /states/<id>
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def dsiplayFilter():
    """display a page"""
    states = storage.all("State").values()
    amn = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amn)


@app.teardown_appcontext
def teardown_db(exception):
    """calls close method of storage"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
