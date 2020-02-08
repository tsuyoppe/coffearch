from django.db import models

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

class Coffee(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    alias = models.CharField(max_length=255, null=True)
    body = models.FloatField()
    acidity = models.FloatField()
    bitterness = models.FloatField()

class CoffeeFlavor(models.Model):
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    flavor = models.CharField(max_length=255)