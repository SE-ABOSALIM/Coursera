from django.urls import path
from . import views

urlpatterns = [
    path('foods/<str:name>', views.food_by_id, name="foods")
]