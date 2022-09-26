from distutils.command.upload import upload
from email.policy import default
from itertools import product
from pyexpat import model
from random import choices
from tkinter import CASCADE
from typing_extensions import Self
from unittest.mock import DEFAULT
from django.db import models
from matplotlib.pyplot import title
from sqlalchemy import true
from django.utils.safestring import mark_safe
DEFAULT_STATUS="draft"
STATUS=[
    ("draft","Taslak"),
    ('published',"Yayinlandi"),
    ('deleted','Silindi')
]


class Category(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField(
        max_length=200,
        default="",
    )
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"



class Product(models.Model):
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        
    )
    title=models.CharField(max_length=200)
    slug=models.SlugField(
        default="",
        max_length=200
        

    )
    cover_image=models.ImageField(
        upload_to="coverimages/",
        null=True,
        blank=True,

    )
    colour=models.CharField(max_length=15)
    products_high=models.PositiveIntegerField()
    products_genislik=models.PositiveIntegerField()
    products_depth=models.PositiveIntegerField()
    foot_colour=models.CharField(max_length=15)
    material=models.CharField(max_length=20)
    tree=models.CharField(max_length=20)
    price=models.FloatField()
    is_home = models.BooleanField(default=False)
    status=models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title


#Çoklu resim için
    def image_tag(self):

        return mark_safe('<img src="{}"height = "50"/>'.format(self.cover_image.url))

    image_tag.short_description = 'Image'

# çoklu resim için sınıf 

class Product_Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    images = models.ImageField(blank=true,upload_to="images")

    def __str__(self) -> str:
        return self.product.title