# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask import render_template
from flask.blueprints import Blueprint

blueprint = Blueprint('dashboard', __name__)


@blueprint.route('/')
def index():
    return render_template('dashboard.html')
