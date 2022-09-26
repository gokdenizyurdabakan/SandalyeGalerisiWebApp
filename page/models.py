from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices

DEFAULT_STATUS="draft"

STATUS = [

    #sol kısım dbye gözükecek sağ kısım admin panelinde kullanana gözükecek sol evrensel sağ bireysel gibi düşünebiliriz#
    #virgülün ikinci kısmını human readable olması için yaptık ileride site çevrilmek istenirse diye #
    ('draft','Taslak'),
    ('published','Yayinlandi'),
    ('deleted','Silindi'),


]


# class Page(models.Model):
#     title =  models.CharField(max_length=200)
#     slug = models.SlugField(
#         max_length=200,
#         default = ""
#     ) #Başta yapmış olsaydık default değer vermek zorunda kalmayacaktık fakat daha önceden oluşturduğumuz sayfalar olduğu için bunun yaptık   # #2# django admin site -djanga admin slug prepopulated_fields yazarak dokümandan bulduk #
#     content = models.TextField()
#     cover_image = models.ImageField(
#         upload_to='page',
#         null=True,
#         blank = True,

#     )
#     status = models.CharField(
#          default=DEFAULT_STATUS,
#          choices=STATUS,
#          max_length=10,
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    

class Carousel(models.Model):
    title = models.CharField(max_length=200,blank=True,null=True) 
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank = True,
    )
    status= models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)