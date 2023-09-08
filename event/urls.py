from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from event.views.eventviews import CreateViewset 
from event.views.inscriptions import subscribe, unsubscribe, myEventSubscribe, eventPast, listEventGroup
from event.views.infoevent import detailEvent, listEvent

routers = DefaultRouter()
routers.register('create-event', CreateViewset, basename='event')

urlpatterns = [
    path('event/', include(routers.urls)),
    path('event/subscribe/', subscribe, name='subscribe'),
    path('event/unsubscribe/', unsubscribe, name='unsubscribe'),
    path('event/myeventsubscribe/', myEventSubscribe, name='myEventSubscribe'),
    path('event/eventPast/', eventPast, name='eventPast'),
    path('event/listEventGroup/', listEventGroup, name='listEventGroup'),
    path('event/detailevent/', detailEvent, name='detailEvent'),
    path('event/listevent/', listEvent, name='listEvent'),
    
]
