from flask import Flask
from flask import request
from flask import jsonify
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required
from flask_jwt_extended import create_access_token
from base_api import BaseAPI


app = Flask('__main__')
base = BaseAPI()
app.config['JWT_SECRET_KEY'] = \
base.config['api']['jwt_secret_key']
jwt = JWTManager(app)

############### testing view ###############

from test_form_view import test_view
if base.config['testing']['test_view']:
	index_view = test_view

else:
	index_view = 'Service is up.'

############################################


@app.route('/', methods=['GET'])
def index():
	print(type(index))
	return index_view

@app.route('/create-user', methods=['POST'])
def create_user():
	try:
		success = base.create_user(request)
		if success:
			success = {'msg': 'Successfully created user.'}
			return jsonify(success), 200
		error = {'msg': 'Create user operation failed.'}
		return jsonify(error)
	except Exception as e:
		base.log_data(str(e))
		error = {'msg': 'Create user operation failed.'}
		return jsonify(error)


@app.route('/login-user', methods=['POST'])
def login_user():
	try:
		success = base.login_user(request)
		if success:
			user_name = request.form.get('user_name')
			access_token = create_access_token(identity=user_name)
			return jsonify(access_token=access_token), 200
		error = {'msg': 'Login failed.'}
	except Exception as e:
		base.log_data(str(e))
		error = base.get_meaningful_error(e)
		return jsonify({'msg':error})


@app.route('/update-user', methods=['POST'])
def update_user():
	try:
		success = base.update_user(request)
		if success:
			response = {'msg': 'Successfully updated user profile.'}
			return jsonify(response), 200
		error = {'msg': 'Update user operation failed.'}
		return jsonify(error)
	except Exception as e:
		# base.log(str(e))
		# error = base.get_meaningful_error(e)
		return jsonify({'msg': str(e)})


@app.route('/login-driver', methods=['POST'])
def login_driver():
	pass


@app.route('/create-trip', methods=['POST'])
def create_trip():
	try:
		success = base.create_trip(request)
		if success:
			response = {'msg': 'Successfully created trip.'}
			return jsonify(response), 200
		error = {'msg': 'Create trip operation failed.'}
		return jsonify(error)
	except Exception as e:
		base.log_data(str(e))
		error = base.get_meaningful_error(e)
		return jsonify(error)


@app.route('/get-trip-by-start-lat-long', methods=['POST'])
def get_trip_by_start_lat_long():
	try:
		trip = base.get_trip_by_start_lat_long(request)
		return jsonify(trip), 200
	except Exception as e:
		base.log_data(str(e))
		error = base.get_meaningful_error(e)
		return jsonify(error)


@app.route('/get-user-by-name/<user_name>', methods=['GET'])
@jwt_required
def get_user(user_name):
	try:
		user = base.get_user_by_name(user_name)
		return jsonify(user), 200
	except Exception as e: 
		base.log_data(str(e))
		error = {'msg': 'Get user operation failed.'}
		return jsonify(error)


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
		return jsonify(error)


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8888)