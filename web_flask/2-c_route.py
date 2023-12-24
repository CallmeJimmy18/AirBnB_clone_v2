#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """ defines an index function """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ defines the function hbnb """
    return "HBNB"


@app.route("/c/<text>")
def C_text(text):
    """ defines the function c_text """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
