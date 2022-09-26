from tkinter import Image
from django.contrib import admin

from products.models import Category, Product, Product_Images

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=(
        "pk",
        "title",
        "slug",
        "status",
        "updated_at",
    )
    list_filter=(
        "status",
        
    )

    list_editable=(
        "status",
        "title",
    )


#Çoklu resim için
class ProductImageInline(admin.TabularInline):
    model = Product_Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=(
        "pk",
        "title",
        "price",
        'cover_image',
        "slug",
        "status",
        "updated_at",
    )
    list_filter=(
        "status",

    )
    list_editable=(
        "status",
        "title",
    )
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Product_Images)