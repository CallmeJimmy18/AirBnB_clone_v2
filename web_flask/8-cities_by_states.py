#!/usr/bin/python3
""" This is a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception):
    """ calls the storage close method """
    storage.close()


@app.route("/cities_by_states")
def cities_by_states():
    """ This displays an HTML page """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
