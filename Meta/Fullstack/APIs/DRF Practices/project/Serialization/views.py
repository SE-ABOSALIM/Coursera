from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from .models import Food, MenuItem, Category
from .serializers import ( 
    FoodsSerializer, 
    FoodsFilteredSerializer, 
    MenuItemSerializer, 
    CategorySerializer 
)

# Standart way
@api_view(['GET'])
def foods_menu(request):
    # without serialization (price_after_tax isn't included)
    # foods = Foods.objects.all()
    # return Response(foods.values())

    # with serialization (price_after_tax field added)
    food_item = Food.objects.all()
    serialized_items = FoodsSerializer(food_item, many=True)
    return Response(serialized_items.data)

# with serializer ('origin' name changed to 'country')
@api_view(['GET'])
def foods_menu_item(request, pk):
    food_item = Food.objects.get(pk=pk)
    serialized_items = FoodsSerializer(food_item)
    return Response(serialized_items.data)

# with filtered serializer for all foods (if we have sernsitive data that we wouldn't display it we need to use filtered serializer)
@api_view(['GET'])
def foods_menu_filtered(request):
    foods = Food.objects.all()
    serialized_and_filtered = FoodsFilteredSerializer(foods, many=True)
    return Response(serialized_and_filtered.data)

# with filtered serializer for a specific food
@api_view(['GET'])
def foods_menu_item_filtered(request, pk):
    foods_item = Food.objects.get(pk=pk)
    serialized_and_filtered = FoodsFilteredSerializer(foods_item)
    return Response(serialized_and_filtered.data)

# ----------------------------------------------------------------------------------

@api_view(['GET', 'POST'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        serialized_items = MenuItemSerializer(items, many=True, context={'request': request}) # we need to provide the context so DRF could extract url field like (port, host, scheme, etc.) from the request object
        return Response(serialized_items.data)
    # To make that work go to serializers.py in the MenuItemSerializer class comment the first category variable and uncomment the second
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def single_menu_item(request, pk):
    item = MenuItem.objects.get(pk=pk)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serialized_category = CategorySerializer(category)
    return Response(serialized_category.data)