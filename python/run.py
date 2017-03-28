import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	connect()
	return "Hello World!"

def connect():
	try:
		connection = mysql.connector.connect(
			user		= "root", 
			password	= "", 
			host		= "mysql", 
			port		= 3306,
			database	= ""
		)
		cursor = connection.cursor(dictionary=True)
	except mysql.connector.Error as err:	
		print("MySQL Connector Error: {}".format(err))
		raise

		return
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)