from xml.etree.ElementInclude import include
from django.urls import path
from .views import RoomView

urlpatterns = [
    path('room', RoomView.as_view()),
]