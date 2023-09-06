from django.db import models

class Group(models.Model):
    nomGroup = models.CharField(max_length=125, default='')
    lieux = models.CharField(max_length=125)
    centre