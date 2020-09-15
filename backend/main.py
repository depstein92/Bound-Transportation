import configparser
from flask import Flask
from flask import request
from base_api import BaseAPI


app = Flask('__main__')
base = BaseAPI()
config = configparser.ConfigParser()
config.read('bound_transportation.cfg')

@app.route('/', methods=['GET'])
def index():

	return 'service is up.'



if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True, port=8888)