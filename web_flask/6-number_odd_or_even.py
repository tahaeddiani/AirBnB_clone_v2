#!/usr/bin/python3
"""t6"""
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


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """is it a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('6-number_template.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    return render_template(
        '6-number_odd_or_even.html', n=n, even_or_odd=even_or_odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
