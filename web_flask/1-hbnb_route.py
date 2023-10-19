#!/usr/bin/python3
"""t1"""
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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
