# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import session, jsonify, request
from flask.blueprints import Blueprint

from dashboard.services.api import APIService


blueprint = Blueprint('menus', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    api_service = APIService(session.get('token'))  # get user's SSO token from session

    return jsonify(api_service.get_menus)
