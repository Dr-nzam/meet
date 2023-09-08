from django.contrib import admin

# Register your models here.
from event.models import Evenement,Participe,CentreInteret,SousCentreInteret

# Register your models here.

admin.site.register(Evenement)
admin.site.register(Participe)
admin.site.register(CentreInteret)
admin.site.register(SousCentreInteret)