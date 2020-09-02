#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_cities(id=None):
    """ display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    if id is None:
        return render_template(
                "9-states.html",
                states=states,
                find='states')
    for s in states:
        if s.id == id:
            cities = storage.all(City).values()
            return render_template(
                "9-states.html",
                states=s,
                find='State',
                cities=cities)
    return render_template(
            "9-states.html")


@app.teardown_appcontext
def close_db(close):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
