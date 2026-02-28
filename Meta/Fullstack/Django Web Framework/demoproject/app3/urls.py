from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('greet', views.greet),
    path('display_year', views.display_year),
]