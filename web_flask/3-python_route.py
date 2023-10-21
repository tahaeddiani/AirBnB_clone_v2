#!/usr/bin/python3
"""t3"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """home func"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb func"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def TextHbnb(text):
    """Text hbnb func"""
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Text hbnb func"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
