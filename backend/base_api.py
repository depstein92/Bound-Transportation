import random
import configparser
from datetime import datetime
from db import bt_db
from db import User
from db import Driver
from db import Trip


class BaseAPI:
	
	def __init__(self):
		self.user = User
		self.driver = Driver
		self.trip = Trip
		self.config = configparser.ConfigParser()
		self.config.read('bound_transportation.cfg')

	def create_user(self, request):
		kwargs = {}
		kwargs['user_name'] = request.form.get('user_name')
		kwargs['user_created']=datetime.now()
		user = self.user(**kwargs)
		user.save()
		return 0

	def create_driver(self, request):
		kwargs = {}
		kwargs['driver_name'] = \
		request.form.get('driver_name')
		kwargs['driver_created']=datetime.now()
		driver = self.driver(**kwargs)
		user.save()
		return 0

	def get_user_by_name(self, name):
		user = self.user.get(
			self.user.user_name == name)
		return self.serialize_model(
			model_name='user', model=user)


	def create_trip(self, request):
		kwargs = {}
		kwargs['start_location_lat_long'] = \
		request.form.get('start_location_lat_long')
		kwargs['start_location_street_address'] = \
		request.form.get('start_location_street_address')
		kwargs['destination_lat_long'] = \
		request.form.get('destination_lat_long')
		kwargs['destination_street_address'] = \
		request.form.get('destination_street_address')
		kwargs['current_lat_long'] = \
		request.form.get('current_lat_long')
		kwargs['trip_has_begun'] = False
		kwargs['trip_has_completed'] = False
		kwargs['date_created'] = datetime.now()
		trip = self.trip(**kwargs)
		trip.save()
		return 0

	def get_trip_by_start_lat_long(self, request):
		start_location_lat_long = \
		request.form.get('start_location_lat_long')
		trip = self.trip.get(
			self.trip.start_location_lat_long == \
			start_location_lat_long)
		trip = self.serialize_model('trip', trip)
		return trip


	def get_trip_by_date_created(self, date):
		trip = self.trip.get(self.trip.date_created==date)
		return trip

	# def generate_user_id(self):
	# 	user_id = random.randint(1000000000, 9999999999)
	# 	return user_id

	def serialize_model(self, model_name, model):
		serialized = {}
		for key, value in model.__data__.items():
			values = self.config['serializer_values'][model_name]
			if key in values:
				serialized[key] = value
		return serialized

