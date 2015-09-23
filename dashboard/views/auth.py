# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import request, session
from flask.blueprints import Blueprint

from dashboard.services.auth import AuthService
from dashboard import constants


blueprint = Blueprint('auth', __name__)


@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    """View handler to login a user account, saving the SSO token in the request session
    """

    if request.method == 'GET':
        # return LOGIN page
        return

    # try to login user based on payload
    provider = request.args.get('provider', constants.AUTH_BASIC)

    # get email & password from request.form
    # NOTE: hashing done over on AuthService end, thus need to ensure SSL is used

    auth_service = AuthService()
    token = auth_service.login(request.form, provider=provider)
    if token:
        print(token)
        session['token'] = token


@blueprint.route('/signup')
def signup():
    """View handler to create an account for new user (username & password).

    Specifically, we send an email to the restaurant's email contact account if the user claims to be owner of restaurant.
    """
    return "Signup Page"