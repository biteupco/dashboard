# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import session, jsonify
from flask.blueprints import Blueprint

from dashboard.services.api import APIService


blueprint = Blueprint('restaurants', __name__)


@blueprint.route('/', methods=['GET'])
def index():
    api_service = APIService(session.get('token'))  # get user's SSO token from session

    payload = api_service.get_restaurants
    restaurants = payload['items']
    return jsonify({'restaurants': restaurants})
