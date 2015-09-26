# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask.blueprints import Blueprint
from flask import render_template


blueprint = Blueprint('accounts', __name__)


@blueprint.route('/')
def index():
    return render_template('account.html')
