from django.db import models
from attraction.models import Attraction

class OrderedAttraction(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    travel_time = models.PositiveIntegerField(null=True, blank=True)
    travel_length = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.attraction.name