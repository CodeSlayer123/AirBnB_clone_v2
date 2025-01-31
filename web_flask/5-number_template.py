#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
from flask import render_template
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


@app.route('/python/<text>')
@app.route('/python')
def python(text="is_cool"):
    """returns Python followed by contents of text variable"""
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    """returns n is a number if n is an integer"""
    return "%s is a number" % n


@app.route('/number_template/<int:n>')
def number_template(n):
    """returns HTML page if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
