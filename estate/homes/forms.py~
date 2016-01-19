from django.forms import ModelForm
from homes.models import *
from django.contrib.auth.models import User

class UserRegisterForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password','first_name','last_name']
		
		
class UserLoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','password']
