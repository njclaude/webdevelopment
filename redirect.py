#!/usr/bin/env python

from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def my_browser():
    return redirect('https://www.facebook.com/')

if __name__ == '__main__':
    app.run(port=2000, debug=True)