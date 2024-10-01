from django.urls import path
from .views import (
    register_user
)


urlpatterns = [
    path('sign-up/', register_user, name='register'),
]