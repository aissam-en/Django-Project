from django.db import models

# Create your models here.


from django.utils import timezone
from users_app.models import Client
from events_app.models import Events

class Tickets(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    match = models.ForeignKey(Events, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    TICKET_TYPES = (
        ('Regulier', 'Regulier'),
        ('VIP', 'VIP'),
    )
    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPES, default='Regulier')

    nbr = models.IntegerField(default=1)

    def __str__(self):
        return  f'Ticket : {self.match.match}'