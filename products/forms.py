from dataclasses import field
from pyexpat import model
from unicodedata import category
from django import forms
from .models import Category,Product,Product_Images


class CategoryModelForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = (
            "title",
            "status",
   )

class ProductModelForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            "category",
            "title",
            "cover_image",
            "colour",
            "products_high",
            "products_genislik",
            "products_depth",
            "foot_colour",
            "material",
            "tree",
            "price",          
            "is_home",
            "status",
            
        ]


class ProductImageModelForm(forms.ModelForm):
    class Meta:
        model = Product_Images
        fields=[
            "product",
            "title",
            "images",
        ]

    
            


    
    
    
    
    
    
    
    
    
    
     