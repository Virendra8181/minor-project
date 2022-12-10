
from django.contrib import admin
from product.models import Product

class Farm_task(admin.ModelAdmin):
     list_display = ('title','slug','content','created_on','items','price','products_name','product_type','image')

admin.site.register(Product,Farm_task)  


	

# Register your models here.
