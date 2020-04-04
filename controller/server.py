#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=missing-module-docstring,missing-function-docstring,invalid-name

from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return "Thermal Comfort Sensing"

@app.route("/csv")
def csv():
    df = pd.read_csv("test.csv")
    df_str = df.to_string()
    print(df_str)
    return df_str.replace("\n", "<br>")
