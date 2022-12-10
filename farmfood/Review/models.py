from django.db import models

class Reviewss(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Subject=models.CharField(max_length=100)
    message=models.TextField()