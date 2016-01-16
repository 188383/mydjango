from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader 
from .models import Room,User

# Create your views here.

def index(request):
	text = 'Index page, fuck PHP'
	template = loader.get_template('homes/index.html')
	context = {
		'text': text,
	}
	return HttpResponse(template.render(context,request))
	
	
def about(request):
	text = 'This is the about page that tells us about the website'
	return HttpResponse(text)
#	a list of the rooms that have been added by users

def list_rooms(request):
	response = 'This is the list of all the rooms'
	return HttpResponse(response)
#	operations on a room that will have an id passed.
#	If the room has an ID we can perform updates on it
# 	note django doesn't support PUT and DELETE
def rooms(request,room_id=None):
	try:
		room = Room.objects.get(pk=room_id)
	except User.DoesNotExist:
		raise Http404('Room does not exist')
	return render(request,'homes/room.html',{'room': room})
	

