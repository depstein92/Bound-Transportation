from flask import Flask
from flask import request
from flask import jsonify
from base_api import BaseAPI

app = Flask('__main__')
base = BaseAPI()

@app.route('/', methods=['GET'])
def index(notification=None):
	if notification:
		return notification
	# TODO: serve web app too ... 
	return 'Service is up.'


@app.route('/create-user', methods=['POST'])
def create_user():
	try:
		success = base.create_user(request)
		return success
	except Exception as e:
		base.log_data(str(e))
		response = {
			'Error': 'Create user operation failed.'
		}
		return jsonify(response)


@app.route('/create-trip', methods=['POST'])
def create_trip():
	try:
		success = base.create_trip(request)
		return success
	except Exception as e:
		base.log_data(str(e))
		response = {
			'Error': 'Create trip operation failed.'
		}
		return jsonify(response)

@app.route('/get-trip-by-start-lat-long', methods=['POST'])
def get_trip_by_start_lat_long():
	try:
		trip = base.get_trip_by_start_lat_long(request)
		return jsonify(trip)
	except Exception as e:
		base.log_data(str(e))
		response = {
			'Error': 'Get trip operation failed.'
		}
		return jsonify(response)


@app.route('/get-user-by-name/<user_name>', methods=['GET'])
def get_user(user_name):
	try:
		user = base.get_user_by_name(user_name)
		return jsonify(user)
	except Exception as e: 
		base.log_data(str(e))
		response = {
			'Error': 'Get user operation failed.'
		}
		return jsonify(response)


@app.route('/get-user-by-name', methods=['POST'])
def get_user_by_post():
	try:
		user_name = request.form.get('user_name')
		user = base.get_user_by_name(user_name)
		return jsonify(user)
	except:
		base.log_data(str(e))
		response = {
			'Error': 'Get user operation failed.'
		}
		return jsonify(response)



if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8888)