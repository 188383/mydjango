from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^about/$',views.about,name='home'),
	url(r'^rooms/?$',views.list_rooms,name='list_rooms'),
	url(r'^rooms/(?P<room_id>[0-9]+)/?$',views.rooms,name='rooms'),
]
