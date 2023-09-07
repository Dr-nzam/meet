from django.urls import path,include
from rest_framework.routers import DefaultRouter
from group.views.group import GroupViewsets
from group.views.inscription import Infogroup
from group.views.message import MessageGroup

routers = DefaultRouter()
routers.register('create-group',GroupViewsets, basename='create-group'),
routers.register('info-group',Infogroup,basename='group'),
routers.register('message',MessageGroup,basename='message'),

urlpatterns = [
    path('/',include(routers.urls)),
    path('a',include('rest_framework.urls'))
    ]
