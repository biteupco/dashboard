# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import

from flask.blueprints import Blueprint
from flask import session, redirect, url_for


blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def main():
    if session.get('token'):
        # user is logged in
        return redirect(url_for('dashboard.index'))

    return redirect(url_for('auth.login'))

