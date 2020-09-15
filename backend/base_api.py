from db import User
from db import Driver
from db import Trip


class BaseAPI:
	
	def __init__(self):
		self.user = User
		self.driver = Driver
		self.trip = Trip

	def get_user_by_name(self, name):
		user = self.user.get(self.user.user_name==name)

		return user

	def get_trip_by_date_created(self, date):
		trip = self.trip.get(self.trip.date_created==date)

		return trip