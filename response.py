
from flask import Flask, request,  make_response

app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('user-Agent')
    response = make_response('<h1>The Browser request is: %s</h1>' % user_agent)
    return response

# app.add_url_rule('/')

if __name__ == '__main__':
    app.run(debug=True)