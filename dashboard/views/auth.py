# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import request, session, redirect, render_template, url_for
from flask.blueprints import Blueprint

from dashboard.services.auth import AuthService
from dashboard.libs.exceptions import HTTPInternalServerError
from dashboard import constants


blueprint = Blueprint('auth', __name__)

LOGIN_FORM_KEYS = ['email', 'password']
SIGNUP_FORM_KEYS = LOGIN_FORM_KEYS + ['first_name', 'last_name']


@blueprint.route('/login', methods=['POST', 'GET'])
def login():
    """View handler to login a user account, saving the SSO token in the request session"""

    if request.method == 'GET':
        # return LOGIN page
        return render_template('auth/login.html')

    # try to login user based on payload
    provider = request.args.get('provider', constants.AUTH_BASIC)
    redirect_url = request.args.get('redirect')

    # get email & password from request.form
    # NOTE: hashing done over on AuthService end, thus need to ensure SSL is used

    auth_service = AuthService()
    payload = {key: request.form.get(key) for key in LOGIN_FORM_KEYS}
    token = auth_service.login(payload, provider=provider)
    if token:
        session['token'] = token
        if redirect_url:
            return redirect(redirect_url)
        return redirect(url_for('menus.index'))  # defaults to menu list

    raise HTTPInternalServerError("error logging in")



@blueprint.route('/signup', methods=['POST', 'GET'])
def signup():
    """View handler to create an account for new user (username & password).

    Verification of user is responsibility of Auth Service
    """
    if request.method == 'GET':
        # return LOGIN page
        return render_template('auth/signup.html')

    provider = request.args.get('provider', constants.AUTH_BASIC)

    payload = {key: request.form.get(key) for key in SIGNUP_FORM_KEYS}
    payload['display_name'] = "{first_name} {last_name}".format(**payload)
    FORBIDDEN_KEYS = ['hash', 'verification_code']
    for key in FORBIDDEN_KEYS:
        if key in payload:
            payload.pop(key)  # remove unwanted attributes in payload

    auth_service = AuthService()
    token = auth_service.signup(payload, provider=provider)
    if token:
        session['token'] = token
        return redirect(url_for('menus.index'))

    raise HTTPInternalServerError("error trying to signup")