"""farmfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from email.mime import image
from unicodedata import name
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name="home"),
    path("products",views.product,name="products"),
    path('categories',views.cat,name="categories"),
    path('contactus',views.contactus,name="contactus"),
    path('veg',views.veg,name="veg"),
    path('dairy',views.Dairy,name="dairy"),
    path('food',views.Food,name="food"),
    path('cart',views.cart,name="cart"),
    path('search',views.search,name= "search"),
    path('control',views.Login.loginpage ,name="control"),
    path('login',views.Login.login,name="login"),
    path('signup',views.Login.signup,name='signup'),
    path('save',views.Login.handelsignup,name='save'),
    path('logout',views.Login.logout,name='logout'),
    path('review',views.Review,name="review"),
    path('order',views.order,name="order"),
    
   
    
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT) 
