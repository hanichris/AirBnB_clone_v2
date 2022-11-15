#!/usr/bin/python3
"""Instantiate an object of class Flask.

The Flask instance is configured to listen on
`0.0.0.0` on port 5000 to have the server available
externally.
"""
from flask import Flask
from flask import escape


app = Flask(__name__)
app.config["SERVER_NAME"] = "0.0.0.0:5000"


@app.route('/', strict_slashes=False)
def hello():
    """Home page of the web application."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display the HBNB page."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Display C followed by the value of `text`.

    Any underscores present in the value of text are
    replaced with a space.
    """
    return "C %s" % escape(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
