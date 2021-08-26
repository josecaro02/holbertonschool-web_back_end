#!/usr/bin/env python3
''' Flask base module'''

from flask import Flask
import flask
from flask_babel import Babel

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    ''' config babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ return 0-index template"""
    return flask.render_template('0-index.html')


if __name__ == "__main__":
    app.run()
