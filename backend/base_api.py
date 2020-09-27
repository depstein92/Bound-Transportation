import configparser
import io
import logging
import random
from datetime import datetime
import boto3
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from db import bt_db
from db import User
from db import Driver
from db import Trip
from error_mapping import known_errors


class BaseAPI:
	
	def __init__(self):
		self.user = User
		self.driver = Driver
		self.trip = Trip
		self.config = configparser.ConfigParser()
		self.config.read('bound_transportation.cfg')
		self.log = self.config['logging']['output']
		self.logging = logging.basicConfig(
			filename=self.log, 
			filemode='w', 
			format='%(name)s - %(levelname)s - %(message)s')
		self.s3 = boto3.client('s3')


	def create_user(self, request):
		"""Create a user.

		Parameters
		----------
		
		request : obj
			
			A Flask `request` object.

		Returns
		-------
		
		1: int
		"""
		kwargs = {}
		raw_password = request.form.get('password')
		hashed_password = generate_password_hash(raw_password)
		kwargs['user_name'] = request.form.get('user_name')
		kwargs['password'] = hashed_password
		kwargs['user_created'] = datetime.now()
		user = self.user(**kwargs)
		user.save()
		return 1

	def create_driver(self, request):
		"""Create a driver.

		Parameters
		----------
		
		request : obj
			
			A Flask `request` object.

		Returns
		-------
		
		1: int
		"""
		kwargs = {}
		kwargs['driver_name'] = \
		request.form.get('driver_name')
		kwargs['driver_created'] = datetime.now()
		driver = self.driver(**kwargs)
		user.save()
		return 1

	def update_user(self, request):
		# user_name = get_jwt_identity()
		user_name = 'jeff' # simple testing setup
		user = self.user.get(
			self.user.user_name == user_name)

		# parse request
		profile_image = request.files['file']

		# read file as bytes stream to keep everything in memory
		image_stream = io.BytesIO(profile_image.stream.read())

		# payment hash if we end up using Stripe
		payment_hash = request.form.get('payment_hash')

		# apply update rules
		if profile_image:
			image_url = self.upload_image(image_stream, user_name)
			user.profile_image_url = image_url

		# if payment_hash:
		# 	user.payment_hash = payment_hash
		user.save()
		return 1


	def login_user(self, request):
		user_name = request.form.get('user_name')
		password = request.form.get('password')
		user = self.user.get(
			self.user.user_name == user_name)
		if check_password_hash(user.password, password):
			return 1
		return 0


	def get_user_by_name(self, name):
		"""Get a user by username.

		Parameters
		----------
		
		name: str
			
			The unique `user_name` of the user being requested.

		Returns
		-------
		
		user: dict
			
			The product of serializing the User model.
		"""
		user = self.user.get(
			self.user.user_name == name)
		user = self.serialize_model(
			model_name='user', model=user)
		return user


	def create_trip(self, request):
		"""Create a trip.

		Parameters
		----------
		
		request: obj
			
			A Flask `request` object.

		Returns
		-------
		
		1: int
		"""
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
		return 1

	def get_trip_by_start_lat_long(self, request):
		"""Get a trip by start latitude and longitude.

		Parameters
		----------
		
		request: obj
			
			A Flask `request` object.

		Returns
		-------
		
		trip: dict
			
			The product of serializing the Trip model.
		"""
		start_location_lat_long = \
		request.form.get('start_location_lat_long')
		trip = self.trip.get(
			self.trip.start_location_lat_long == \
			start_location_lat_long)
		trip = self.serialize_model(
			model_name='trip', model=trip)
		return trip


	def get_trip_by_date_created(self, request):
		"""Get a trip by the date that it was created.

		Parameters
		----------
		
		request: obj
			
			A Flask `request` object.

		Returns
		-------
		
		trip: dict
			
			The product of serializing the Trip model.
		"""
		trip = self.trip.get(
			self.trip.date_created==datetime)
		trip = self.serialize_model(
			model_name='trip', model=trip)
		return trip

	# def generate_user_id(self):
	# 	user_id = random.randint(1000000000, 9999999999)
	# 	return user_id

	def serialize_model(self, model_name, model):
		"""Serialize Peewee database models.

		Parameters
		----------
		
		model_name: str
			
			The lowercase name of the model to be serialized.
		
		model: obj
			
			The model to be serialized.

		Returns
		-------
		
		serialized: dict
			
			The serialized model.
		"""
		serialized = {}
		values = self.config['serializer_values'][model_name]
		for key, value in model.__data__.items():
			if key in values:
				if type(value) not in ['datetime']:
					serialized[key] = str(value)
				serialized[key] = value
		return serialized

	def log_data(self, msg):
		logging.warning(msg)

	def get_meaningful_error(self, e):
		for key, value in known_errors.items():
			if key in str(e):
				msg = value
				return msg
		msg = 'Operation failed. Unknown error...'
		return msg

	def upload_image(self, profile_image, user_name):
		self.s3.upload_fileobj(profile_image, "bound-transportation", user_name, ExtraArgs={ "ContentType": "image/jpeg"})
		response = self.s3.generate_presigned_url(
			'get_object',
			Params={
				'Bucket': 'bound-transportation',
				'Key': user_name
			})
		print(response)
		return response


