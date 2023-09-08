
from django.db import models
from account.models import CustomUser
from group.models import Group
# Create your models here.

class CentreInteret(models.Model):
    categories = models.CharField(max_length=128)
    image = image = models.FileField(upload_to='assets/cat/', blank=True)
    
    def __str__(self):
        return self.categories 
    
class Evenement (models.Model):
    nomEvent = models.CharField(max_length=128)
    type = models.CharField(max_length=128)
    lieux = models.CharField(max_length=128)
    DateEvent = models.CharField(max_length=128, default=0)
    categories = models.ForeignKey(CentreInteret, on_delete=models.CASCADE, related_name='eventcat', null= True, blank=True)
    description = models.TextField()
    image = models.FileField(upload_to='assets/images/', blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='eventgroup', null= True, blank=True)
    
    def __str__(self):
        return self.nomEvent
    
    
class Participe (models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='event', null=True, blank=True)
    user  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='event1', null=True, blank=True)
    
    
class SousCentreInteret(models.Model):
    nom = models.CharField(max_length=128)
    centreInteret = models.ForeignKey(CentreInteret, on_delete=models.CASCADE, related_name='souscat', null= True, blank=True)
    
    def __str__(self):
        return self.nom