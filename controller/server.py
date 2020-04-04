#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Thermal Comfort Sensing"
