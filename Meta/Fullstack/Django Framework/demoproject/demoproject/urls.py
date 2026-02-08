from django.contrib import admin 
from django.urls import path, include
from app import views

urlpatterns = [ 
    path('demo/', views.index, name='index'), # name='index' alias for demo page
    path('', include('app2.urls')),
]