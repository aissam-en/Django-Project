from django.db import models
from django.utils import timezone

from users_app.models import Organisateur

# Create your models here.

class Events(models.Model):
    match = models.CharField(max_length=255)
    date = models.DateField(default=timezone.now)
    lieu = models.CharField(max_length=255)
    
    organisateur = models.ForeignKey(Organisateur, on_delete=models.CASCADE, related_name='events')

    image = models.ImageField(upload_to='images', default='default.png', blank=True)

    def __str__(self):
        return self.match
