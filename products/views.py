from itertools import product
from .forms import CategoryModelForm, ProductImageModelForm,ProductModelForm
from .models import Category,Product, Product_Images
from contextvars import Context
from django.utils.text import slugify
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

#Index 


# def index(request):
#     context = dict()

#     products = Product.objects.filter(
#         status = "published",#Burası status olursa yazdırılmaz published olması lazım çünkü burası filter kısmı olması gerekenleri eklediğimiz kısım 
#         is_home=True,
#     ).exclude(cover_image='')

#     context['products'] = products
#     return render(request,"index.html",context)

#Category

def category_show(request,category_slug):
    context = dict()
    context["category"]  = get_object_or_404(Category,slug=category_slug)
    context["items"]  = Product.objects.filter(
        category=context['category'],
        status="published",
    )
    return render(request,"base.html",context)
@staff_member_required
def Category_Create(request):
    
    context=dict()
    context["title"] = "Ürün Grubu Oluşturma"
    context["form"] = CategoryModelForm
    if request.method == "POST":
        print(request.POST)
        (request.FILES.get("cover_image"))
        form = CategoryModelForm(request.POST,request.FILES)

        if form.is_valid(): 
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Ürün Grubu Başarıyla Eklendi ")
            
    return render(request,"manage/form.html",context) 
    

def Category_List(request):
    context=dict()
    context["items"] = Category.objects.all().order_by("-pk")
    return render(request,"manage/category_list.html",context)

def Category_update(request,pk):
    context=dict()
    item = Category.objects.get(pk=pk)
    context["title"] = f"{item.title}-pk:{item.pk} Kategori Güncelleme Formu"
    context["form"] = CategoryModelForm(instance=item)
    if request.method == "POST":
        form = CategoryModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Kategori Başarıyla Güncellendi ")
            return redirect("category_list")
            

    return render(request,"manage/form.html",context)

def Category_delete(request,pk):
    item = Category.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect("category_list")




#Product
@staff_member_required
def Product_create(request):
    context=dict()
    context["title"] = "Ürün Oluşturma"
    context["form"] =ProductModelForm
    if request.method == "POST":
        print(request.POST)
        (request.FILES.get("cover_image"))
        form = ProductModelForm(request.POST,request.FILES)

        if form.is_valid(): 
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Ürün Başarıyla Eklendi ")
            
      
    return render(request,"manage/form.html",context)
def product_list(request):
    context=dict()
    context["product"] = Product.objects.all().order_by("-pk")
    return render(request,"manage/product_list.html",context)


def product_update(request,pk):
    context=dict()
    item = Product.objects.get(pk=pk)
    context["title"] = f"{item.title}-pk:{item.pk} Ürün Güncelleme Formu"
    context["form"] = ProductModelForm(instance=item)
    if request.method == "POST":
        form = ProductModelForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Ürün Başarıyla Güncellendi ")
            return redirect("product_list")

    return render(request,"manage/form.html",context)

def product_delete(request,pk):
    item = Product.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect("product_list")


def productimage_fields(request):
    context=dict()
    context["title"] = "Ürün fotoğrafları ekleme"
    context["form"] = ProductImageModelForm
    if request.method == "POST":
        print(request.POST)
        (request.FILES.get("cover_image"))
        form = ProductImageModelForm(request.POST,request.FILES)

        if form.is_valid(): 
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace("ı","i"))
            item.save()
            messages.success(request,"Fotoğraflar başarıyla eklendi")
            
    return render(request,"manage/form.html",context) 
    
def product_show(request,product_slug):
    context = dict()
    context["product"]  = get_object_or_404(Product,slug=product_slug)
    context["items"]  = Product.objects.filter(
        status="published",
    )
    context["image"]=Product_Images.objects.all()
    return render(request,"product_show.html",context)