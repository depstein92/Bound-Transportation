from flask import Flask
from flask import request
from flask import jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from base_api import BaseAPI

app = Flask('__main__')
base = BaseAPI()
app.config['JWT_SECRET_KEY'] = \
base.config['api']['jwt_secret_key']
jwt = JWTManager(app)


@app.route('/', methods=['GET'])
def index():
	return 'Service is up.'

@app.route('/create-user', methods=['POST'])
def create_user():
	try:
		success = base.create_user(request)
		if success:
			success = {'msg': 'Successfully created user.'}
			return jsonify(success), 200
		response = {'msg': 'Create user operation failed.'}
		return jsonify(response)
	except Exception as e:
		base.log_data(str(e))
		response = {'msg': 'Create user operation failed.'}
		return jsonify(response), e[0][0]['code']

@app.route('/login-user', methods=['POST'])
def login_user():
	try:
		success = base.login_user(request)
		user_name = request.form.get('user_name')
		access_token = create_access_token(identity=user_name)
		return jsonify(access_token=access_token), 200
	except Exception as e:
		base.log_data(str(e))
		response = {'msg': 'Login failed.'}
		return jsonify(response), e[0][0]['code']


@app.route('/login-driver', methods=['POST'])
def login_driver():
	pass


@app.route('/create-trip', methods=['POST'])
def create_trip():
	try:
		success = base.create_trip(request)
		success = {'msg': 'Successfully created trip.'}
		return jsonify(success), 200
	except Exception as e:
		base.log_data(str(e))
		error = {'msg': 'Create trip operation failed.'}
		return jsonify(error), e[0][0]['code']

@app.route('/get-trip-by-start-lat-long', methods=['POST'])
def get_trip_by_start_lat_long():
	try:
		trip = base.get_trip_by_start_lat_long(request)
		return jsonify(trip), 200
	except Exception as e:
		base.log_data(str(e))
		error = {'msg': 'Get trip operation failed.'}
		return jsonify(error), e[0][0]['code']


@app.route('/get-user-by-name/<user_name>', methods=['GET'])
@jwt_required
def get_user(user_name):
	try:
		user = base.get_user_by_name(user_name)
		return jsonify(user), 200
	except Exception as e: 
		base.log_data(str(e))
		error = {'msg': 'Get user operation failed.'}
		return jsonify(error), e[0][0]['code']


@app.route('/get-user-by-name', methods=['POST'])
@jwt_required
def get_user_by_post():
	try:
		user_name = request.form.get('user_name')
		user = base.get_user_by_name(user_name)
		return jsonify(user), 200
	except Exception as e:
		base.log_data(str(e))
		error = {'msg': 'Get user operation failed.'}
		return jsonify(error), e[0][0]['code']


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8888)