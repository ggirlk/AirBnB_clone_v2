#!/usr/bin/python3
""" Hello Flask """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello HBNB!'
