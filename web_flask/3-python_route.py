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


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """funtion that display “C ” followed by
    the value of the text variable after /c/<text>"""
    if "_" in text:
        text = text.replace("_", " ")
    return "c %s" % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """ display “Python ”, followed by the value of
    the text variable after /python/<text> or /python"""
    text = text.replace("_", " ")
    return "Python %s" % text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
