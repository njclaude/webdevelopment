#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/counter/<int:value>')
def counter(value):
    my_dict = {1: 'Number One', 2: 'Number Two', 3: 'Number Three', 4: 'Number Four', 5: 'Number Five'}

    while value <= 5:
        if value in my_dict.keys():
            return my_dict[value]
        else:
            return 'Unknown Number'


if __name__ == '__main__':
    app.run(debug=True)