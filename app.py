#!/usr/bin/env python

from flask import Flask, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return make_response('<h1>Hello world</h1>')

if __name__ == '__main__':
    app.run(port=2000, debug=True)