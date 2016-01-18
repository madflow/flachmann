#!/usr/bin/env python
# -*- coding: utf-8 -*-

from {{cookiecutter.app_name}}.app import app

app.run(use_reloader=True, debug=True)
