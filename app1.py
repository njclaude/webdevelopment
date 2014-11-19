#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)


@app.route('<kigali')
def index():
    return "Hello kigali %s "

if __name__ == '__main__':
    app.run(debug=True)

