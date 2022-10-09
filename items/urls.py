from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name = 'index'),
    path("shop/", shop, name = 'shop'),
    path("contact/", contact, name = 'contact')
]