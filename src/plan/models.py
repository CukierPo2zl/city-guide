from django.db import models
from django.conf import settings
from ordered_attraction.models import OrderedAttraction

class Plan(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    route = models.ManyToManyField(OrderedAttraction)
    route_length = models.FloatField(default=0.0)


    def __str__(self):
        return str(self.id)

