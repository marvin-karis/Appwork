from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm

from .models import product
# Create your views here.


def product_create_view(request):
    my_form = ProductForm(request.POST or None)
    if my_form.is_valid():
        # now data is good
        print(my_form.cleaned_data)
        my_form.save()
        my_form = ProductForm()
        product.objects.create(my_form.cleaned_data)
    else:
        print(my_form.errors)
    context = {
        "form": my_form
    }
    return render(request, "Product/product_create.html", context)


def product_update_view(request, id=id):
    # print(request.GET)
    # print(request.POST)
    obj = get_object_or_404(product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    # if request.method== "POST":
    #    my_new_title = request.POST.get('title')
    #    print(my_new_title)
    # product.objects.create(title=my_new_title) saves to the satabase
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "Product/product_create.html", context)


def product_detail_view(request):
    obj = get_object_or_404(product, id=id)
    # context = {
    # 'title' : obj.title,
    # 'description': obj.description
    #    'object' : obj
    # }
    context = {
        'object': obj
    }
    return render(request, "Product/detail.html", context)


def dynamic_lookup_view(request, id):
    #obj = product.objects.get(id=1)
    #obj = get_object_or_404(product, id=id)
    try:
        obj = product.objects.get(id=id)
    except product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "Product/product_list.html", context)


def product_list_view(request):
    queryset = product.objects.all()  # lists all objects
    context = {
        "object_list": queryset
    }
    return render(request, "Product/product_list.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(product, id=id)
    if request.method == "POST":
        # confirming delete
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }
    return render(request, "Product/product_delete.html", context)
