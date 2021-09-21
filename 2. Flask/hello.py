# MVC (Model View Controller)

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello World</h1>'


@app.route("/user/<name>")
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route("/headers")
def headers():
    user_agent = request.headers.get('User-Agent')
    return 'Your Browser is: %s' % user_agent


if __name__ == '__main__':
    app.run(debug=True)
