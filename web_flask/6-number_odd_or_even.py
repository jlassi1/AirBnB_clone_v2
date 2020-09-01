#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template

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
    text = text.replace("_", " ")
    return "C %s" % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythoniscool(text="is cool"):
    """ display “Python ”, followed by the value of
    the text variable after /python/<text> or /python"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route("/number/<int:n>", strict_slashes=False)
def find_int(n):
    """display “n is a number” only if n is an integer
    after /number/<n>"""
    return "%d is a number" % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY"""
    return render_template("5-number.html", N=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n is even|odd” inside the tag BODY"""
    return render_template("6-number_odd_or_even.html", N=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
