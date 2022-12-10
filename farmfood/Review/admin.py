from email import message
from django.contrib import admin
from Review.models import Reviewss

class ReviewAdmin(admin.ModelAdmin):
    list_admin=('Name','Email','Subject','message')
    
admin.site.register(Reviewss,ReviewAdmin)

# Register your models here.
