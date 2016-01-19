from django import forms
from homes.models import *
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
		