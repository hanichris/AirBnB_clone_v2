#!/usr/bin/python3
"""Instantiate an object of class Flask.

The Flask instance is configured to listen on
`0.0.0.0` on port 5000 to have the server available
externally.
"""
from flask import Flask


app = Flask(__name__)
app.config["SERVER_NAME"] = "0.0.0.0:5000"
