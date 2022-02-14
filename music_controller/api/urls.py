from xml.etree.ElementInclude import include
from django.urls import path
from .views import main

urlpatterns = [
    path('', main, name='main'),
]