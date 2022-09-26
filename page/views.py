from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from page.models import Carousel
from .forms import CarouselModelForm
from django.utils.text import slugify
from django.contrib.admin.views.decorators import staff_member_required
from products.models  import Category, Product

STATUS = "published"

#User:
def index(request):
    """    context = dict()
    context ["images"] =Carousel.objects.filter(
        status = "published",

    ).exclude(cover_image = "")"""
    images = Carousel.objects.filter(
        status = "published" 
    
    ).exclude(cover_image = "")#cover imagesi yoksa demek 
    
    context = {
        "images":images
    }
    context["images"]=images
    products = Product.objects.filter(
        is_home=True,
        status = STATUS,

    )
    context['products']=products
    #if not request.session.session_key:
       # request.session.save()
    
    return render(request,"index.html",context)

def manage_list(request):
    context = dict()
    return render(request,"manage/manage.html",context)

#PAGE:

# @staff_member_required
# def page_list(request):
#     context=dict()
#     context["items"] = Page.objects.all().order_by("-pk")
#     return render(request,"manage/page_list.html",context)

# def page_create(request):
#     context = dict()
#     context["title"] = "Page Create Form"
#     context["form"]=PageModelForm()
#     if request.method == 'POST':
#         print(request.POST)
#         (request.FILES.get("cover_image"))
#         form=PageModelForm(request.POST ,request.FILES)
        
#         if form.is_valid():
#             item = form.save(commit=False)
#             item.slug = slugify(item.title.replace("ı","i"))
#             item.save()
#             messages.success(request,"Birseyler eklendi")
#     return render(request,"manage/form.html",context)

# def page_update(request,pk):# pk primary key = id istememizin nedeni unic kodla çağıracak olmamız
#     context = dict()
#     item = Page.objects.get(pk=pk)
#     context["title"] = f"{item.title} - pk:{item.pk} Carousel Update Form"
#     context["form"]  = PageModelForm(instance=item)
#     if request.method == "POST":
#         form = PageModelForm(request.POST,request.FILES , instance=item)
#         if form.is_valid():
#             item = form.save(commit=False)
#             if item.slug == "":
#                 item.slug = slugify(item.title.replace("ı","i"))
#             item.save()
            
#             #return redirect("carousel_list") burası carousel liste gider bu şekildede yapılabilir aşağıdaki şekildede yapılabilir 
#             messages.success(request,"Güncelleme Başarıyla Gerçekleşti")
#             return redirect("page_update",pk)
#     return render (request,"manage/form.html",context)
# def page_delete(request,pk):
#     item=Page.objects.get(pk=pk)
#     item.status = "deleted"
#     item.save()
#     return redirect("page_list")

#CAROUSEL:

@staff_member_required
def carousel_list(request):
    context=dict()
    context["carousel"] = Carousel.objects.all().order_by("-pk")
    return render(request,"manage/carousel_list.html",context)

def carousel_update(request,pk):# pk primary key = id istememizin nedeni unic kodla çağıracak olmamız
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context["title"] = f"{item.title} - pk:{item.pk} Carousel Update Form"
    context["form"]  = CarouselModelForm(instance=item)
    if request.method == "POST":
        form = CarouselModelForm(request.POST,request.FILES , instance=item)
        if form.is_valid():
            form.save()
            #return redirect("carousel_list") burası carousel liste gider bu şekildede yapılabilir aşağıdaki şekildede yapılabilir 
            messages.success(request,"Güncelleme Başarıyla Gerçekleşti")
            return redirect("carousel_update",pk)
    return render (request,"manage/form.html",context)

def carousel_create(request):
    context = dict()
    context["title"] = "Carousel Create Form"
    context["form"]=CarouselModelForm()
    if request.method == 'POST':
        print(request.POST)
        (request.FILES.get("cover_image"))
        form=CarouselModelForm(request.POST ,request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request,"Birseyler eklendi ama ne olduğnu bilmiyorum","manage/carousel.html")
    return render(request,"manage/form.html",context)

def hakkimizda(request):
    return render(request,"hakkimizda.html")