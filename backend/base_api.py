import random
import datetime
from db import User
from db import Driver
from db import Trip


class BaseAPI:
	
	def __init__(self):
		self.user = User
		self.driver = Driver
		self.trip = Trip

	def create_user(self, request):
		user_name = request.form.get('user_name')
		user_id = self.generate_user_id()
		user = self.user(
			user_name=user_name,
			user_id=user_id)
		user.save()
		return 0

	def get_user_by_name(self, name):
		user = self.user.get(self.user.user_name==name)
		return {'user_name':user.user_name, 'user_id':user.user_id}

	def create_trip(self, request):
		start_location_lat_long = request.form.get('start_location_lat_long')
		start_location_street_address = request.form.get('start_location_street_address')
		destination_lat_long = request.form.get('destination_lat_long')
		destination_street_address = request.form.get('destination_street_address')
		current_lat_long = request.form.get('current_lat_long')
		trip_has_begun = False
		trip_has_completed = False
		date_created = datetime.now()
		trip = self.trip(
			start_location_lat_long=start_location_lat_long,
			start_location_street_address=start_location_street_address,
			destination_lat_long=destination_lat_long,
			destination_street_address=destination_street_address,
			current_lat_long=current_lat_long,
			trip_has_begun=trip_has_begun,
			trip_has_completed=trip_has_completed)
		trip.save(force_insert=True)
		return 0

	def get_trip_by_date_created(self, date):
		trip = self.trip.get(self.trip.date_created==date)
		return trip

	def generate_user_id(self):
		user_id = random.randint(1000000000, 9999999999)
		return user_id
