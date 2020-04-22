#!/usr/bin/python3
""" Hello Flask """


from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c():
    return 'C %s' % escape(text)


@app.route('/python/<text>', strict_slashes=False)
def python():
    str = escape(text)
    str = str.replace(' ', '_')
    return 'Python %s' % str

if __name__ == "__main__":
    app.run()
