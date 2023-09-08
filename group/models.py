from django.db import models
from account.models import CustomUser

class Group(models.Model):
    namGroup = models.CharField(max_length=125, default='')
    places = models.CharField(max_length=125, default='')
    centerInterest = models.CharField(max_length=200, default='')
    description = models.TextField(default='New group')
    imageGroup = models.FileField(upload_to='assets/imagesgroup/', blank=True, null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='usercreategroup', null=True, blank=True)
    
    def __str__(self):
        return self.namGroup

class Inscription(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group', null=True, blank=True)
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='usergroup', null=True, blank=True)

class Message(models.Model):
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='usergroupmessage', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groupmessage', null=True, blank=True)
    message = models.TextField()