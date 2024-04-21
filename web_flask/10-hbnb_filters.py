#!/usr/bin/python3
"""
Installed and utilising flask for a dynamic feel
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Get all State objects from storage (sorted by name)"""
    states = sorted(storage.all("State").values(), key=lambda state: state.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the SQLAlchemy session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
