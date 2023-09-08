from django.urls import path,include
from rest_framework.routers import DefaultRouter
from group.views.group import GroupViewsets
from group.views.inscription import subscribe, unsubscribe, listMember, numberMember, myGroup
from group.views.message import sendMessageGroup, listMessageGroup

routers = DefaultRouter()
routers.register('create-group',GroupViewsets, basename='create-group'),

urlpatterns = [
    path('group/',include(routers.urls)),
    path('group/subscribe-group/<int:idgroup>/<int:iduser>/', subscribe, name='subscribe'),
    path('group/unsubscribe-group/<int:idgroup>/<int:iduser>/', unsubscribe, name='unsubscribe'),
    path('group/list-member-group/<int:idgroup>/', listMember, name='listMember'),
    path('group/list-number-group/', numberMember, name='numberMember'),
    path('group/list-group-user-subscribe/', myGroup, name='myGroup'),
    path('group/add-message/', sendMessageGroup, name='sendMessageGroup'),
    path('group/list-message/', listMessageGroup, name='group/list-message/'),
    ]
