# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask.blueprints import Blueprint
from flask import render_template, session

from dashboard.services.api import APIService


blueprint = Blueprint('accounts', __name__)


@blueprint.route('/')
def index():
    token = session.get('token')
    user_id = session.get('user_id')

    api_service = APIService(token)  # get user's SSO token from session
    user_json = api_service.get_user(id=user_id)
    params = {
        'user': user_json
    }
    return render_template('account.html', **params)
