from django.shortcuts import render
from .models import Foods

def food_by_id(request, name):
    foods = Foods.objects.all()
    context = {
        'foods': foods,
        'name': name
    }
    return render(request, 'display_foods.html', context)
