from django.shortcuts import render
from django.http import Http404,HttpResponse

#from django.template import loader 
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
	
def user_rooms(request, user_id=None):
	try:
		owner = User.objects.get(id=user_id)
		rooms = Room.objects.filter(owner = owner)
	except User.DoesNotExist:
		raise Http404('Url error, check user id')
	return render(request,'homes/user_rooms.html',{'rooms':rooms,'owner':owner.username})

