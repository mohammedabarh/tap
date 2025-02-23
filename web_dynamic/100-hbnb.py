#!/usr/bin/python3
"""Flask application to create a complete HTML page with location and amenity
dropdown menus along with rental listings."""
from flask import Flask, render_template
from models import storage
import uuid

app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/100-hbnb')
def display_hbnb():
    """Render a page featuring dropdown menus for states and cities."""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    cache_id = uuid.uuid4()
    return render_template('100-hbnb.html',
                           states=states,
                           amenities=amenities,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close the database or file storage when the request ends."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
