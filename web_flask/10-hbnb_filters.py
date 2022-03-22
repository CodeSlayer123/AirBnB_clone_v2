#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models import amenity
from models.amenity import Amenity
from models.state import State
import os

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """tears down database"""
    storage.close()


@app.route('/hbnb_filters')
def filters():
    """returns HTML page"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    #state = None
    #flag = 0
    #if id:
    #    for item in states.values():
    #        if item.id == id:
    #            state = item
    #            flag = 1

    #    return render_template('9-states.html', states=states,
    #                           state=state, id=item.id, flag=flag)
    #else:

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
