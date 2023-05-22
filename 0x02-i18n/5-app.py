#!/usr/bin/env python3
"""0-app
"""

import getopt
from typing import Union
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext
import greenlet

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Available languges and defaults"""
    LANGUAGES = ['en', 'fr']

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


def get_locale() -> str:
    """Determines best match for supported languages"""
    locale = request.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


def get_user() -> Union[dict, None]:
    """ return user dict if ID can be found
    """
    login_as = request.args.get('login_as', False)
    if login_as:
        user = users.get(int(login_as), False)
        if user:
            return user
    return None


@app.before_request
def before_request():
    """use get_user and set user as a global on flask.g.user
    """
    g.user = get_user()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """renders template"""
    if g.user:
        return render_template('5-index.html',
                               title=gettext('home_title'),
                               header=gettext('home_header'),
                               username=g.user['name'])
    else:
        return render_template('5-index.html',
                               title=gettext('home_title'),
                               header=gettext('home_header'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
