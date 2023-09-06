from django.urls import path
from group.views.group import GroupViewsets

urlpatterns = [
    path('group/create-group/', GroupViewsets, name='create-group' )
]
