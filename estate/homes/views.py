from django.shortcuts import render
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import login as L,authenticate as A

#from django.template import loader 
from .models import Room

from django.contrib.auth.models import User
from homes.forms import UserRegisterForm,UserLoginForm

# Create your views here.

def index(request):
	text = 'Index page, fuck PHP'
	#template = loader.get_template('homes/index.html')
	context = {
		'text': text,
	}
	#return HttpResponse(template.render(context,request))
        return render(request,'homes/index.html',context)
	
	
def about(request):
	text = 'This is the about page that tells us about the website'
	return HttpResponse(text)
#	a list of the rooms that have been added by users

def list_rooms(request):
	params = request.GET
	limit = 5
	skip = 0
	try:
		limit = params['limit']
		skip = params['skip']
	except:
		limit = 5
		skip = 0
		
	header = 'list of rooms '
	
	rooms = Room.objects.all()[skip:limit]
	
	#read the generic views documentation to decide whether this app needs the generic views module
	return render(request,'homes/rooms.html',{'rooms':rooms,'header':header})

#	operations on a room that will have an id passed.
#	If the room has an ID we can perform updates on it
# 	note django doesn't support PUT and DELETE
def rooms(request,room_id=None):
	try:
		room = Room.objects.get(pk=room_id)
	except Room.DoesNotExist:
		raise Http404('Room does not exist')
	return render(request,'homes/room.html',{'room': room})
	

# lists the rooms that belong to a specific user
def user_rooms(request, user_id=None):
	try:
		owner = User.objects.get(id=user_id)
		rooms = Room.objects.filter(owner = owner)
	except User.DoesNotExist:
		raise Http404('Url error, check user id')
	return render(request,'homes/user_rooms.html',{'rooms':rooms,'owner':owner.username})


#login page, remember the redirect for post requests, seen here in else, which should process the form appropriately

def login(request):
	if request.method == 'GET':
		form = UserLoginForm
		return render(request,'homes/login_form.html',{'form':form})
	else:
		 username = request.POST['username']
		 password = request.POST['password']
		 	
		 user = A(username=username,password=password)
		 if user.is_active:
		 	L(request,user)
		 
		 return HttpResponse(str(user) + " has been logged in!")
		 
def register(request):
# we have received a request to register a user
	if request.method == 'POST':
		return HttpResponse(request.POST['username'])
	else:
		form = UserRegisterForm
                return render(request,'homes/register_forms.html',{'form':form})
	
	
		 
