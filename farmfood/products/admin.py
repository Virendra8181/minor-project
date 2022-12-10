from django.contrib import admin
from products.models import Products
class ProductsAdmin(admin.ModelAdmin):
    list_admin=('Name','Price','Products_type','Product_tit','product_image','Products_ID')
    
admin.site.register(Products,ProductsAdmin)
# Register your models here.
