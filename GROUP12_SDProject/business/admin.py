from django.contrib import admin
from .models import Product,Business,Category


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class BusinessAdmin(admin.ModelAdmin):
    pass
admin.site.register(Business, BusinessAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

