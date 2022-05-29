from django.shortcuts import render
from .models import services

# Create your views here.
def services_detail_view(request):
    obj = services.objects.get(id=1)
    context = {
        'title' : obj.title,
        'description': obj.description
    }
    return render (request, "services/services.html", {})