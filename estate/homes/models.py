from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class User(models.Model):
#
#	def __str__(self):
#		return self.username
#
#	name = models.CharField(max_length=200)
#	surname = models.CharField(max_length=200)
#	username = models.CharField(max_length=200)
#	password = models.CharField(max_length=200)
#	role = models.CharField(max_length=200)
#
class Room(models.Model):
	def __str__(self):
		return str(self.user)
	owner = models.ForeignKey(User,on_delete=models.CASCADE)
	user = models.IntegerField()

	

