from django.urls import path
from notification.views.notification import (in_out_groupNotification,userSubcribeEventNotification,
                                            emailConfirmNotification,subscribeEventNotification,newEventNotification)

urlpatterns = [
    path('notification/in_out_groupNotification/',in_out_groupNotification, name='in_out_groupNotification'),
    path('notification/userSubcribeEventNotification/',userSubcribeEventNotification, name='userSubcribeEventNotification'),
    path('notification/emailConfirmNotification/',emailConfirmNotification, name='emailConfirmNotification'),
    path('notification/subscribeEventNotification/',subscribeEventNotification, name='sendComment'),
    path('notification/newEventNotification/',newEventNotification, name='newEventNotification'),
    
]
