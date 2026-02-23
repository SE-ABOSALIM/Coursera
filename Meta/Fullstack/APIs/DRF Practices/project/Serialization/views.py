from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage
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
        # Searching | Filtering | Ordering | Pagination splits large datasets into smaller pages to improve performance and make API responses easier to consume.
        category_name = request.query_params.get('category') # filter parameter
        price = request.query_params.get('price') # filter parameter
        search = request.query_params.get('search') # search parameter
        order = request.query_params.get('order') # Order parameter
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        if category_name: # title(model-field)__lookup(rule-to-apply)
            items = items.filter(category__title=category_name) # filtering based on category name
        if price: 
            items = items.filter(price=price) # filtering based on price
        if search: 
            items = items.filter(title__icontains=search) # searching based on url search parameter's value
        if order:
            # items = items.order_by(order) # ordering based on a model field
            order_fields = order.split(',')
            items = items.order_by(*order_fields) # ordering based on more than one model field togather
        # ----------------------------------------------------------------------------------------------------
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except:
            items = []
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