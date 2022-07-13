from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

response = requests.get('https://api-mobilespecs.azharimm.site/v2/brands/')


# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def main_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "main.html", {})


def about_view(request, *args, **kwargs):
    with response as brand:
        brand = response.json()
        brands = brand["data"]
    # my_context = {

        # "title": "templete tags and filter",
        # "my_number": 123,
        # "my_list": [333, 666, 999]

    # }

    return render(request, "about.html", {
        # 'Id': brands.brand_id,
        # 'Name': brands.brand_name,
        # 'slug': brands.brand_slug,
        # 'Count': brands.device_count
        'brands': brands
    })


def services_view(request, *args, **kwargs):
    return render(request, "services.html", {})


def style(request):
    return render(request, 'home.html')
