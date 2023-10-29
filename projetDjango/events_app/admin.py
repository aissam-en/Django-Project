from django.contrib import admin
from .models import Events

# Register your models here.
# admin.site.register(Events)


# pour l'organisateur doit gerer just ses evemenets 
from users_app.models import Organisateur
class EventAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        try:
            organisateur = Organisateur.objects.get(id=request.user.id)
        except Organisateur.DoesNotExist:
            organisateur = None

        if request.user.is_superuser or request.user.groups.filter(name='admin_group').exists():
            # Administrateur voir all events
            print('------------------# Administrateur voir all events')
            return qs
        elif request.user.groups.filter(name='organisateur_group').exists():
            # pour l'organisateur doit gerer just ses evemenets
            print('-----------------# pour l organisateur doit gerer just ses evemenets ')
            return qs.filter(organisateur=organisateur)
        else:
            # autre users can not acces au evenemets
            print('------------------# autre users can not acces au evenemets')
            return qs.none()

admin.site.register(Events, EventAdmin)