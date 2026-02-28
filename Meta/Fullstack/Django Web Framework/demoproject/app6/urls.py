from django.urls import path
from . import views

urlpatterns = [
    path('colors/<str:color>', views.show_colors, name='show_colors')
]