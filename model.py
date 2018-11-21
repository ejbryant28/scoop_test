
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Token(db.Model):
	"""A table for all the possible acceptable tokens along with their types"""

	__tablename__ = 'tokens'

	#This table is meant to maintain to maintain the referencial integrity of the requests table
		#If someone tries to make a request that the API doesn't support, it'll make error handling easier and faster
		#It'd also make it easy to expand the requests supported in the future (such as allowing division or multiplication)

	value = db.Column(db.VARCHAR(1), primary_key = True)
	token_type = db.Column(db.String(20), nullable = False)


class Calculation(db.Model):
	
	__tablename__ = 'calculations'

	# calc_id = db.Column(db.VARCHAR(100), primary_key = True)
	calc_id = db.Column(db.Integer, primary_key = True)

class Request(db.Model):
	"""This table is to track all the requests made to the API
	 
	"""

	__tablename__ = 'requests'

	request_id = db.Column(db.Integer, primary_key = True)
	# calc_id = db.Column(db.VARCHAR(100), nullable = False)
	calc_id = db.Column(db.Integer, db.ForeignKey('calculations.calc_id'), nullable = False)
	token = db.Column(db.VARCHAR(1), db.ForeignKey('tokens.value'), nullable = False)
	time_requested = db.Column(db.DateTime, nullable = False)


	tokens = db.relationship("Token", backref=db.backref("requests"))
	calculation = db.relationship("Calculation", backref = db.backref('requests'))


def connect_to_db(app, database):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = database
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    print("Connected to DB")


if __name__ == "__main__":

    from server import app  
    connect_to_db(app, 'postgres:///calculator') 
    db.create_all() 