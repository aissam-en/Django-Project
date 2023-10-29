from django.contrib import admin
from .models import Admininstrateur,Client,Organisateur, Users

# Register your models here.
admin.site.register(Users)
admin.site.register(Admininstrateur)
admin.site.register(Client)
admin.site.register(Organisateur)