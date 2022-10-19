
from django.db import models

# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.district

class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    city = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.city