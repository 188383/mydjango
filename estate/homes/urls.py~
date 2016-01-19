from django.conf.urls import url

from . import views

# when adding app_name to the urlConf file, we are namespacing the urls for the templating system.
#another change is the structure of the templates directory
app_name = 'homes'
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^about/$',views.about,name='about'),
	url(r'^rooms/?$',views.list_rooms,name='list_rooms'),
	url(r'^rooms/(?P<room_id>[0-9]+)/?$',views.rooms,name='rooms'),
	url(r'^user/(?P<user_id>[0-9]+)/?$',views.user_rooms, name= 'user_rooms'),
	url(r'^login/?$',views.login,name="login"),
	url(r'^register/?',views.register,name="register"),
]
