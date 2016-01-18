from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
	def __str__(self):
		return str(self.owner)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	floorspace = models.IntegerField()
        people = models.IntegerField()
        cost = models.DecimalField(max_digits=12,decimal_places=2)
        floorlevel = models.IntegerField()
        lift = models.BooleanField()
        garden = models.BooleanField()
        parking = models.BooleanField()
        kitchen = models.BooleanField()
        bathroom = models.BooleanField()
        bath = models.BooleanField()
        shower = models.BooleanField()
        floorheating = models.BooleanField()
        aircon = models.BooleanField()
        washmachine = models.BooleanField()
        pets = models.BooleanField()
        television = models.BooleanField()
        catering = models.BooleanField()
        disabled = models.BooleanField()
        swimmingpool = models.BooleanField()
        interenet = models.BooleanField()
        #Remember that the pictures url has to be created when the user registers the room on the system
        picturesurl = models.CharField(max_length = 200)
        children = models.BooleanField()

# address for a concrete house or room

class Address(models.Model):
        latitude = models.DecimalField(max_digits = 10, decimal_places=8)
        longitude = models.DecimalField(max_digits = 10, decimal_places=8)
        address_full = models.CharField(max_length = 400)
        house_number = models.IntegerField()
        country = models.CharField(max_length = 300)
        region = models.CharField(max_length = 300)
        city = models.CharField(max_length = 300)
        room = models.ForeignKey(Room, on_delete = models.CASCADE)

# This is the users booking model. This holds all the vital information with regards to the room

class UserBooking(models.Model):
        room = models.ForeignKey(Room,on_delete= models.CASCADE)
        client = models.ForeignKey(User,on_delete = models.CASCADE)
        arrivaldate = models.DateField()
        departuredate = models.DateField()
        rate = models.DecimalField(max_digits = 12, decimal_places = 2)
        people = models.IntegerField()
        identity = models.CharField(max_length=20)
        confirmed = models.BooleanField()

# This is the rating model. The user is allowed to rate provided he/she has been to the location

class RoomRating(models.Model):
        room = models.ForeignKey(Room, on_delete=models.CASCADE)
        user = models.ForeignKey(User,on_delete=models.CASCADE)
        rating = models.IntegerField() 
        comment = models.CharField(max_length=160)
        booking = models.ForeignKey(UserBooking,on_delete = models.CASCADE)
        
        
