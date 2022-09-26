from django import forms 
from .models import Carousel

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model=Carousel
        #fields = '__all__' # Bunu kullanmak sağlıklı değil 
        fields = [
            "title",
            "cover_image",
            "status",
        ]

# class PageModelForm(forms.ModelForm):
#     class Meta:
#         model = Page 
#         #fields='__all__'
#         #exclude=['title']
#         fields = [
#             'title',
#             'cover_image',
#             'content',
#             'status',
#         ]