from django.shortcuts import render
from django.http import HttpResponse

from .models import Country

def index(request):
    country_list = Country.objects.order_by('continent')
    context = {
        'countries': [
            {'name': country.name }
            for country in country_list
            ]
    }
    return render(request, 'coffearch/index.html', context)

def detail(request, country_name):
    return HttpResponse(f'this page is {country_name} detail page!!')
