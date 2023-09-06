# voice_interface_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat, name="chat"),
    path("index/", views.index, name="index"),
]
