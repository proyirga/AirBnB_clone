#!/usr/bin/python3
"""a script that starts a Flask web application:
    Requirements:
    The web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    You must use the option strict_slashes=False in the route definition
"""

from flask import Flask
"""Starting app"""


app = Flask(__name__)


"""Routing to a root of the module"""
@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
