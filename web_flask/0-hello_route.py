#!/usr/bin/python3
"""Flask web application."""
from web_flask import app


@app.route('/', strict_slashes=False)
def hello():
    """Home page of the web application."""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
