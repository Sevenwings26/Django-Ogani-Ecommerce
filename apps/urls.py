from django.urls import path
from .views import *


urlpatterns = [

    path('', index, name='home'),
    # auth 
    # path('register/', register, name="register" ), 

    # pages 
    path('shop/', shop, name='shop'),
    path('blog-view/', blog, name='blog'),
    path('contact-us/', contact, name='contact'),

]