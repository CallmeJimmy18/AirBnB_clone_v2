#!/usr/bin/python3
""" This is a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', strict_slashes=False)
def states():
    """Displays a list of states."""
    states = storage.all("State")
    return render_template('9-states.html', state=states)


@app.route("/states/<id>", strict_slashes=False)
def state_details(id):
    """Displays details of a specific state."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
