#!/usr/bin/env python

from flask import Flask, make_response

app = Flask(__name__)


@app.route('<kigali')
def index():
    return make_response("Hello kigali %s ")

if __name__ == '__main__':
    app.run(debug=True)

