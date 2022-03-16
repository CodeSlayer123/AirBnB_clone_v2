#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_HBNB():
    """returns hello HBNB"""
    return "Hello HBNB!"

@app.route('/hbnb')
def HBNB():
    """returns HBNB"""
    return "HBNB"

@app.route('/c/<text>')
def C(text):
    """returns C followed by contents of text variable"""
    return "C %s" % text.replace("_", " ")

app.run(host="0.0.0.0")