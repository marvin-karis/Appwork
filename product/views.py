from django.shortcuts import render

from .forms import ProductForm

from .models import product
# Create your views here.



def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form 
    }
    return render (request, "Product/product_create.html", context)



def product_detail_view(request):
    obj = product.objects.get(id=1)
    #context = {
        #'title' : obj.title,
        #'description': obj.description
    #    'object' : obj
    #}
    context = {
        'object' : obj
    }
    return render (request, "Product/detail.html", context)  