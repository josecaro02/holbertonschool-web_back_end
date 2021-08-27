#!/usr/bin/env python3
''' Flask base module'''

from flask import Flask, request
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


@babel.localeselector
def get_locale() -> str:
    """ get locale selector to guess user accept language """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ return 0-index template"""
    return flask.render_template('4-index.html')


if __name__ == "__main__":
    app.run()
