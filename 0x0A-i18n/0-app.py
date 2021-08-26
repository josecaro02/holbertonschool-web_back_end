#!/usr/bin/env python3
''' Flask base module'''

from flask import Flask
import flask

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ return 0-index template"""
    return flask.render_template('templates/0-index.html')


if __name__ == "__main__":
    app.run()
