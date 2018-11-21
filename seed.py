from flask_sqlalchemy import SQLAlchemy

from model import *

from server import app

from datetime import datetime


def load_tokens(tokens_dict):
    """Load all the allowed tokens into the table

    I am passing the tokens in as a dictionary, where the keys are the types and the values are a list of acceptable tokens for that type
    """

    for token_type in tokens_dict:

        for token in tokens_dict[token_type]:

            new_token = Token(token_type = token_type, value = token)
            db.session.add(new_token)

    db.session.commit()


def load_calc():

    for n in range(10):
        new_calc = Calculation()
        db.session.add(new_calc)

    db.session.commit()

def load_requests():

    calcs = Calculation.query.all()

    for calc in calcs:
        now = datetime.now()
        new_request = Request(calc_id = calc.calc_id, token = 1, time_requested = now)
        # first = Request(calc_id = "ecc7ab90-0a59-4168-b1e5-b5cf63edf9fd", token = 1, time_requested = now)
        db.session.add(new_request)
    db.session.commit()

    
def load_tests():
    # connect_to_db(app, 'postgres:///calculator')

    tokens = {
        'operator': ['+', '-', '='],
        'number': [ n for n in range(10)],
    }

    load_tokens(tokens)
    load_calc()
    load_requests()

if __name__ == '__main__':

    connect_to_db(app, 'postgres:///calculator')
    load_tests()
