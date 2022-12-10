
from django.db import models



class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    items = models.TextField()
    price=models.IntegerField()
    products_name=models.TextField()
    product_type=models.TextField()
    image = models.ImageField(upload_to='images')
   
    
    

	

	


# Create your models here.
