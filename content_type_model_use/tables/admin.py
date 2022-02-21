from django.contrib import admin

from .models import Product, Book, Cupboard

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Cupboard)
class ProductAdmin(admin.ModelAdmin):
    pass
