"""Appwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from pages.views import home_view, about_view, main_view
from pages import views
from services.views import services_detail_view
from product.views import (
    product_create_view,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view,
    product_update_view,
)


urlpatterns = [
    path('home', home_view),
    path('', main_view),
    path('view', views.style),
    path('about/', about_view),
    path('services/', services_detail_view),
    path('admin/', admin.site.urls),



    path('product/<int:id>/', dynamic_lookup_view, name='product'),
    path('product/create/', product_create_view),
    path('product/<int:id>/update/', product_update_view, name='product-update'),
    path('product/<int:id>/delete/', product_delete_view, name='product-delete'),
    path('product/list/', product_list_view, name='product-list'),
]
