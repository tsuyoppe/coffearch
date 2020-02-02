from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    continent = models.CharField(max_length=50)
    coffee_production = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Region(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
