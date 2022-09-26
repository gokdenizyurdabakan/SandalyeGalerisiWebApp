from django.contrib import admin
from .models import Carousel

# Register your models here.



# class PageAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}
#     list_display = (
#         "pk",
#         "title",
#         "slug",
#         "status",
#         "updated_at",
#     )
#     list_filter=(
#         "status",
        
        
#     )
#     list_editable = (
#         "status",
#         "title",
#     )
class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "title",
        "cover_image",
        "status",
    ]
    list_filter=[
        "status",
        
        
    ]
    list_editale=[list_filter]


# admin.site.register(Page,PageAdmin)
admin.site.register(Carousel,CarouselAdmin)



# MİNİMUM DJANGO YAPISI 
# View yapısı / Control
# Template
# Admin
# Forms
# Message
# Session

