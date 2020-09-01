#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ function that display “Hello HBNB!” after / """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ function that display “HBNB” after /hbnb """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
