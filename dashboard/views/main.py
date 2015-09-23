# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask.blueprints import Blueprint


blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def main():
    return "Welcome to Dashboard"