#!/usr/bin/env python3
"""0-app
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Available languges and defaults"""
    LANGUAGES = ['en', 'fr']

    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """renders template"""
    return render_template('3-index.html',
                           title=gettext('home_title'),
                           header=gettext('home_header'))


def get_locale() -> str:
    """Determines best match for supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
