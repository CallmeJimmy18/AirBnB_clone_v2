#!/usr/bin/python3
""" This is a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exc):
    """ calls the storage close method """
    storage.close()


@app.route("/states_list")
def state_list():
    """ This displays an HTML page """
    states = storage.all(State).values()

    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
