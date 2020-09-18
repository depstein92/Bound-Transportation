from peewee import *

bt_db = SqliteDatabase('bt.db')

class User(Model):
    user_name = CharField(max_length=25, unique=True)
    user_id = AutoField()

    class Meta:
        database = bt_db

class Driver(Model):
    user_name = CharField(max_length=25, unique=True)
    driver_id = AutoField()

    class Meta:
        database = bt_db

class Trip(Model):
	start_location_lat_long = CharField(max_length=100)
	start_location_street_address = CharField(max_length=150)
	destination_lat_long = CharField(max_length=100)
	destination_street_address = CharField(max_length=150)
	trip_has_begun = BooleanField()
	trip_has_completed = BooleanField()
	current_lat_long = CharField(max_length=100)
	date_created = DateTimeField()
	trip_id = AutoField()
	
	class Meta:
		database = bt_db

def initialize_db():
    bt_db.connect()
    bt_db.create_tables([User, Driver, Trip], safe=True)
    bt_db.close()

initialize_db()