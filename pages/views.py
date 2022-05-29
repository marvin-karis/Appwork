from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request ,"home.html",{})

def about_view(request, *args, **kwargs):
    my_context = {
        "title":"templete tags and filter",
        "my_number" : 123,
        "my_list" : [333, 666, 999]
    }
    return render(request ,"about.html", my_context)

def services_view(request, *args, **kwargs):
    return render(request ,"services.html",{})