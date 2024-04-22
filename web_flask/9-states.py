from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    # Get all State objects from storage (sorted by name)
    states = sorted(storage.all("State").values(), key=lambda state: state.name)

    # Render the HTML template
    return render_template('states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Get the State object with the specified ID"""
    state = storage.get("State", id)

    if state:
        """Get all City objects linked to the State (sorted by name)"""
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state_cities.html', state=state, cities=cities)
    else:
        return "<h1>Not found!</h1>"


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Close the SQLAlchemy session after each request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
