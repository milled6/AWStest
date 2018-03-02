
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
	'postgresql+psycopg2://TraderRater1:p4M35-anas+Bo@traderraterpostgresql.crsy502iuh5m.us-west-2.rds.amazonaws.com:5432/TraderRater'

db = SQLAlchemy(app)


class User(db.Model):
	phone_number = db.Column(db.String(10), primary_key=True)
	favorite_color = db.Column(db.String(10))

	def __init__(self, phone_number, favorite_color):
		self.phone_number = phone_number
		self.favorite_color = favorite_color



@app.route('/test/')
def test():
	print("working")
	return "This is what winning looks like"


if __name__ == '__main__':
	print("running")
	db.create_all()
	app.debut = True
	app.port = '5432'
	app.run()



# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'
