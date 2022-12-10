
from django.contrib import admin
from order.models import Customer

class Order(admin.ModelAdmin):
     list_display = ('Cus_ID','product_ID','Addresh','conform')

admin.site.register(Customer,Order) 