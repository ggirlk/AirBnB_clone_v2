#!/usr/bin/python3
""" Hello Flask """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c():
    return 'C %s' % text


if __name__ == "__main__":
    app.run()
