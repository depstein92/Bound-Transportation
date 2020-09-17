import configparser
from flask import Flask
from flask import request
from flask import jsonify
from base_api import BaseAPI

app = Flask('__main__')
base = BaseAPI()
config = configparser.ConfigParser()
config.read('bound_transportation.cfg')


@app.route('/', methods=['GET'])
def index(notification=None):
	if notification:
		return notification
	else:
		return 'service is up.'


@app.route('/create-user', methods=['POST'])
def create_user():
	user = base.create_user(request)
	return jsonify(user)


@app.route('/create-trip', methods=['POST'])
def create_trip():
	trip = base.create_trip(request)
	return jsonify(trip)


@app.route('/get-user-by-name/<user_name>', methods=['GET'])
def get_user(user_name):
		print(user_name)
		if user_name:
			try:
				user = base.get_user_by_name(user_name)
				return jsonify(user)
			except Exception as e:
				print(str(e))
				return index(str(e))
		else: 
			return index(str(e))


@app.route('/get-user-by-name', methods=['POST'])
def get_user_by_post():
	try:
		user_name = request.form.get('user_name')
		user = base.get_user_by_name(user_name)
		return jsonify(user)
	except Exception as e:
		return index(str(e))


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8888)