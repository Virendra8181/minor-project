from distutils.command.upload import upload
from django.db import models

class Products(models.Model):
    Name=models.CharField(max_length=100)
    Price=models.IntegerField()
    Products_type=models.CharField(max_length=100)
    Product_tit=models.CharField(max_length=400)
    product_image= models.ImageField(upload_to='images')
    Products_ID=models.IntegerField(primary_key=True)
   
