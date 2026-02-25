from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
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
from .models import MenuItem
from .serializers import MenuItemSerializer

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

@api_view(['GET', 'POST'])
@permission_classes([IsManager])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.all()
        serialized_items = MenuItemSerializer(items, many=True)
        return Response(serialized_items.data)
    
    if request.method == 'POST':
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item, status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsManager])
def single_menu_items(request, pk):
    if request.method == 'GET':
        item = MenuItem.objects.get(pk=pk)
        serialized_item = MenuItemSerializer(item)
        return Response(serialized_item.data)
    
    if request.method == 'PUT':
        item