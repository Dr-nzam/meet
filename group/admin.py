from django.contrib import admin
from group.models import Group, Inscription, Message
# Register your models here.

admin.site.register(Group)
admin.site.register(Inscription)
admin.site.register(Message)