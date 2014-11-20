
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('user-Agent')
    return '<h1>The Browser requesting is %s</h1>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)