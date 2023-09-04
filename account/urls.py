from django.urls import path
from account.views import register, login

urlpatterns = [
    path('account/register/',register, name='register'),
    path('account/login/',login, name='login'),
]
