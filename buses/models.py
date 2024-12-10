from django.db import models

# Create your models here.
class Busform(models.Model):
    route_no = models.IntegerField()
    bus_no = models.IntegerField()
    number_plate= models.CharField(max_length=5)
    live_location_link = models.URLField()

class Addroutes(models.Model):
    routenum = models.IntegerField()
    areas = models.TextField()

