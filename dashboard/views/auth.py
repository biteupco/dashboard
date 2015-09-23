# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import request, session, redirect, render_template, url_for
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
        return render_template('auth/login.html')

    # try to login user based on payload
    provider = request.args.get('provider', constants.AUTH_BASIC)
    redirect_url = request.args.get('redirect')

    # get email & password from request.form
    # NOTE: hashing done over on AuthService end, thus need to ensure SSL is used

    auth_service = AuthService()
    payload = {key: request.form.get(key) for key in ['email', 'password']}
    token = auth_service.login(payload, provider=provider)
    if token:
        session['token'] = token
        if redirect_url:
            return redirect(redirect_url)
        return redirect(url_for('menus.index'))  # defaults to menu list

    return "token not found"



@blueprint.route('/signup')
def signup():
    """View handler to create an account for new user (username & password).

    Specifically, we send an email to the restaurant's email contact account if the user claims to be owner of restaurant.
    """
    return "Signup Page"