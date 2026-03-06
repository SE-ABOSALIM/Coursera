from django.contrib.auth.models import User, Group
from django.db import transaction
from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import ( 
    api_view, 
    permission_classes, 
    throttle_classes,
)
from rest_framework.permissions import (
    IsAuthenticated, 
    IsAdminUser,
    BasePermission, 
    SAFE_METHODS
)
from rest_framework.throttling import (
    AnonRateThrottle, 
    UserRateThrottle,
)
from .models import (
    MenuItem,
    Cart,
    Order,
    OrderItem,
)
from .serializers import (
    MenuItemSerializer,
    CartSerializer,
    OrderSerializer,
)

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated and
            request.user.groups.filter(name='FP-Manager').exists()
        )

class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated and
            request.user.groups.filter(name='FP-delivery-crew').exists()
        )

class DummyView:
    filter_backends = []

def apply_filters_and_pagination(request, queryset, serializer_class,
                                 filter_fields=None, search_fields=None, ordering_fields=None):
    view = DummyView() 

    # Filtering
    if filter_fields:
        filter_backend = DjangoFilterBackend()
        view.filterset_fields = filter_fields
        queryset = filter_backend.filter_queryset(request, queryset, view)

    # Searching
    if search_fields:
        search_backend = SearchFilter()
        view.search_fields = search_fields
        queryset = search_backend.filter_queryset(request, queryset, view)

    # Ordering
    if ordering_fields:
        ordering_backend = OrderingFilter()
        view.ordering_fields = ordering_fields
        queryset = ordering_backend.filter_queryset(request, queryset, view)

    # Pagination
    paginator = PageNumberPagination()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serializer = serializer_class(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)




@api_view(['GET', 'POST'])
@permission_classes([IsManager])
def menu_items(request):
    if request.method == 'GET':
        queryset = MenuItem.objects.all()
        return apply_filters_and_pagination(
            request,
            queryset,
            MenuItemSerializer,
            filter_fields=['category', 'stock', 'price'],
            search_fields=['title', 'price'],
            ordering_fields=['price', 'stock']
        )
    
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsManager])
def menu_item_details(request, pk):
    
    item = get_object_or_404(MenuItem, pk=pk)
    
    if request.method == 'GET':
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serialized_item = MenuItemSerializer(
            item,
            data=request.data
        )
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    
    if request.method == 'PATCH':
        serialized_item = MenuItemSerializer(
            item,
            data=request.data,
            partial=True
        )
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
@permission_classes([IsManager])
def group_users(request, group_name):

    group = get_object_or_404(Group, name__iexact=group_name)

    if request.method == 'GET':
        users = group.user_set.all()
        data = [{"id": u.id, "username": u.username, "full_name": u.first_name + " " + u.last_name} for u in users]
        return Response(data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        user_id = request.data.get('user_id')
        user = get_object_or_404(User, id=user_id)
        group.user_set.add(user)
        return Response(
            {"message": "User added to group"},
            status=status.HTTP_201_CREATED
        )
    

@api_view(['DELETE'])
@permission_classes([IsManager])
def group_user_detail(request, group_name, id):

    group = get_object_or_404(Group, name__iexact=group_name)
    user = get_object_or_404(User, id=id)

    if user not in group.user_set.all():
        return Response(
            {"error": "User not in this group"},
            status=status.HTTP_404_NOT_FOUND
        )

    group.user_set.remove(user)
    return Response(
        {"message": "User removed from group"},
        status=status.HTTP_200_OK
    )

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_cart(request):

    if request.method == 'GET':
        queryset = Cart.objects.filter(user=request.user).select_related('user')
        serialized_items = CartSerializer(queryset, many=True)
        return Response(serialized_items.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save(user=request.user)
        return Response(serialized_item, status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def orders(request):
    
    user = request.user

    if request.method == 'GET':
        if user.groups.filter(name='FP-Manager').exists():
            queryset = Order.objects.all()
        elif user.groups.filter(name='FP-delivery-crew').exists():
            queryset = Order.objects.filter(delivery_crew=user)
        else:
            queryset = Order.objects.filter(user=user)

        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=user)

        if not cart_items.exists():
            return Response(
                {"detail": "Cart is empty. Cannot create order."},
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():
            order = Order.objects.create(
                user=user,
                status=False,
                total=0,
                date=timezone.now().date(),
                delivery_crew=None
            )

            total_price = 0

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    menuitem=item.menuitem,
                    quantity=item.quantity,
                    unit_price=item.unit_price,
                    final_price=item.final_price
                )
                total_price += item.final_price

            order.total = total_price
            order.save()

            cart_items.delete()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def order_details(request, pk):

    order = get_object_or_404(Order, pk=pk)
    user = request.user

    is_manager = user.groups.filter(name='FP-Manager').exists()
    is_delivery = user.groups.filter(name='FP-delivery-crew').exists()

    if request.method == 'GET':
        if order.user != user and not is_manager and not is_delivery:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = OrderSerializer(order)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        if is_manager:
            serializer = OrderSerializer(order, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)

        elif is_delivery:
            if order.delivery_crew != user:
                return Response(status=status.HTTP_403_FORBIDDEN)

            if 'status' not in request.data:
                return Response(
                    {"detail": "You can only update status."},
                    status=400
                )

            order.status = request.data['status']
            order.save()

            return Response(OrderSerializer(order).data)

        return Response(status=status.HTTP_403_FORBIDDEN)

    if request.method == 'DELETE':
        if not is_manager:
            return Response(status=status.HTTP_403_FORBIDDEN)

        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)