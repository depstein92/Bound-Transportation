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
	return 'service is up.'


@app.route('/create-user', methods=['POST'])
def create_user():
	try:
		success = base.create_user(request)
		return jsonify(success)
	except Exception as e:
		return index(str(e))


@app.route('/create-trip', methods=['POST'])
def create_trip():
	try:
		success = base.create_trip(request)
		return success
	except Exception as e:
		return index(str(e))


@app.route('/get-user-by-name/<user_name>', methods=['GET'])
def get_user(user_name):
	try:
		user = base.get_user_by_name(user_name)
		return jsonify(user)
	except Exception as e: 
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