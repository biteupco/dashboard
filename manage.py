# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
from dashboard import create_app

app = create_app()

# note: turn debug off when in production
app.run(debug=True)
