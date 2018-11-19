##imports
######################################################################################################################################

from jinja2 import StrictUndefined
from flask import (Flask, render_template, redirect, request, flash, session, jsonify)
from flask_debugtoolbar import DebugToolbarExtension


##set up
######################################################################################################################################

app = Flask(__name__)

app.secret_key = "SuperSecretSHHHHHHHH"

app.jinja_env.undefined = StrictUndefined

##routes
######################################################################################################################################
@app.route('/')
def homepage():

    return 'things!'


######################################################################################################################################
if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=5000, host='0.0.0.0')