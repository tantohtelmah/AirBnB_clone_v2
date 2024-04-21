#!/usr/bin/python3
"""
Displays an html page which is running on http://172.29.243.70:5000
if only it is an integer
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ prints a display"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ prints a display"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_custom_text(text):
    """ prints a formatted text"""
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    """ prints a formatted text"""
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ prints a number"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """ prints an htlm page """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
