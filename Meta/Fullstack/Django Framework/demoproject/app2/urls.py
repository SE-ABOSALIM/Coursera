# Better Practice to include the urls.py in app level
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]