#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Piątek"

if __name__ == '__main__':
    app.run(debug=True)
