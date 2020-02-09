from django.contrib import admin

from .models import Country, Region, Coffee, CoffeeFlavor

admin.site.register(Country)
admin.site.register(Region)
admin.site.register(Coffee)
admin.site.register(CoffeeFlavor)