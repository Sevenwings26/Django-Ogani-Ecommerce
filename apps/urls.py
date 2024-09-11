from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    path('blog-view/', blog, name='blog'),
    path('contact-us/', contact, name='contact'),
]