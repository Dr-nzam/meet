from django.db import models
from account.models import CustomUser

class Group(models.Model):
    namGroup = models.CharField(max_length=125, default='')
    places = models.CharField(max_length=125)
    centerInterest = models.CharField(max_length=200)
    description = models.TextField()
    imageGroup = models.FileField(upload_to='assets/imagesgroup/', blank=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='usercreategroup')

class Inscription(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group', null=True, blank=True)
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='usergroup', null=True, blank=True)
    