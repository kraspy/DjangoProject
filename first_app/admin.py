from django.contrib import admin

from first_app.models import Category, Product


# Register your models here.
@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
