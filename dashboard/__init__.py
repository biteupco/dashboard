# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import Flask, jsonify

import os
from flask_compress import Compress
from dashboard.libs import exceptions
from dashboard.services.auth import AuthService


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # for gzip
    Compress().init_app(app)

    # import blueprints
    from dashboard.views import main, auth, accounts, menus, restaurants

    # setup env, secret keys, etc.
    app.secret_key = os.getenv('BENRI_SECRET')  # recommended for setting up Flask session
    AuthService.set_env('dev')

    # main views
    app.register_blueprint(main.blueprint, url_prefix='/')
    app.register_blueprint(auth.blueprint, url_prefix='/auth')

    # user-specific views
    app.register_blueprint(accounts.blueprint, url_prefix='/accounts')
    app.register_blueprint(menus.blueprint, url_prefix='/menus')
    app.register_blueprint(restaurants.blueprint, url_prefix='/restaurants')

    @app.before_request
    def _before_request():
        pass

    @app.errorhandler(exceptions.HTTPBadRequest)
    def handle_http_bad_request(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


    @app.errorhandler(exceptions.HTTPUnauthorized)
    def handle_http_unauthorized(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


    @app.errorhandler(exceptions.HTTPInvalidMethod)
    def handle_http_invalid_method(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app