##imports
######################################################################################################################################

from jinja2 import StrictUndefined
from flask import (Flask, jsonify)
from flask_debugtoolbar import DebugToolbarExtension


##set up
######################################################################################################################################

app = Flask(__name__)

app.secret_key = "SuperSecretSHHHHHHHH"

app.jinja_env.undefined = StrictUndefined

##routes
######################################################################################################################################
@app.route('/calculations', methods = ["GET", "POST"])
def calculations():

    # pass

    if methods == "GET":
        #list all the calculations on the API
        calculations = Calculation.query.all()
        return jsonify(calculations)

    if methods =="POST":
        #creates a new empty calculation
        # calc = randint(0, 1000)
        new_calc = Calculation()
        db.session.add(new_calc)
        calc = {'id': new_calc.calc_id, 'tokens': new_calc.requests} 
        return jsonify(calc)

    # else:
    #     #throw error




@app.route('/calculations/:calculationID/tokens', methods = ["POST"])
def calculation_tokens():
    """Adds a token to an existing calculations"""

    #I am querying for the most recent calculation in case we allow for the same calculation id to be used multiple times, 
    #additionally using the first selector returns 'none' if there are none rather than throwing an error which allows us to implement our own error handling
    calculation = Calculation.query.filter(Calculation.calc_id == calculationID).first()

    #first check to make sure the calculation exists
    if not calculation:
        return 'ERROR'
        #to do: specify, suggest entering new calc

    #if this is the first entry in requests, make sure it's a number
    elif not calculation.requests:

        if tokens['type'] == 'operator':
            return 'ERROR'
            #to do: specify

    #if it's not the first entry, make sure the most recent token was a different type
    #to do: this is wrong right now
    elif tokens['type'] == calculation.requests[-1]:
        return 'ERROR'
            #to do: make this error more specific

    #if all those check have passed, add an entry into the requests table 
    now = datetime.now()
    new_request = Request(calc_id = calculationID, token = tokens['value'], time_requested = now)
    db.session.add(new_request)
    db.session.commit()

    return jsonify(tokens)


@app.route('/calculations/:calculationID/result', methods = ["GET"])
def calculation_result():

    calculation = Calculation.query.filter(Calculation.calc_id == calculationID)

    return calculation.requests




######################################################################################################################################
if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

    app.run(port=5010, host='0.0.0.0')