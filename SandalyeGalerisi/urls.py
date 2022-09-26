"""qrmenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from products.forms import CategoryModelForm
from products.views import ( 
    category_show,
    Category_Create,
    Category_List,
    Category_delete,
    Category_update,
    Product_create,
    product_list,
    product_update,
    product_delete,
    productimage_fields,
    product_show

    
    )
 
from page.views import (
    

    index,
    # page_delete,
    # page_list,
    # page_update,
    # page_create,
    carousel_create,
    carousel_update,
    carousel_list,
    manage_list,
    hakkimizda,
    )


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', index, name="home/index"),
    path('hakkimizda',hakkimizda,name="hakkimizda"),
    #Category
    path('<slug:category_slug>', category_show, name='base'),
    path('manage/category_create/',Category_Create, name="category_create"),
    path('manage/category_list/',Category_List, name="category_list"),
    path('manage/category_delete/<int:pk>/',Category_delete, name="category_delete"),
    path('manage/category_update/<int:pk>/',Category_update, name="category_update"),
    

    #Product
    path('manage/product_create/',Product_create, name="category_update"),
    path('manage/product_list/',product_list, name="product_list"),
    path('manage/product_update/<int:pk>/',product_update, name="product_update"),
    path('manage/product_delete<int:pk>/',product_delete, name="product_delete"),
    path('manage/productimage_fields/',productimage_fields, name="productimage_fields"),
    path('products/<slug:product_slug>', product_show, name='product_show'),
    
    #Manage:
    path('manage/',manage_list, name="manage_list"),
    #Carousel:
    path('manage/carousel_create/',carousel_create, name="carousel_create"),
    path('manage/carousel_list/',carousel_list, name="carousel_list"),
    path('manage/carousel_update/<int:pk>/',carousel_update, name="carousel_update"),
    #Page:
    # path('manage/page_list/',page_list, name="page_list"),
    # path("manage/page_create/",page_create,name="page_create"),
    # path('manage/page_update/<int:pk>/',page_update, name="page_update"),
    # path('manage/page_delete/<int:pk>/',page_delete, name="page_delete"),
    

   
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#Burası resimleri çıkarmaya yarar settings.py kısmında da ayarı var 
