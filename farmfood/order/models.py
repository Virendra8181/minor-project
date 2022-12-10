
from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    Cus_ID= models.ForeignKey(User, on_delete=models.CASCADE)
    product_ID=models.IntegerField()
    Addresh=models.TextField()
    conform=models.BooleanField()




