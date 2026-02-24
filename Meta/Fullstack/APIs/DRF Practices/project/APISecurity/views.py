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
)
from rest_framework.throttling import (
    AnonRateThrottle, 
    UserRateThrottle,
)
from .throttles import TwentyCallsPerMinute

# Authentication and Authorization ----------------------------------------------------------------------------------------

# Authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # If we don't provide the credentials it will give us a 401-Unauthorized response
def secret(request):
    return Response({'message': 'Some secret message'})

# Manager Group Authorization
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({'message': 'Only manager should see this message'})
    else:
        return Response({'message': 'Authorization required for this area'}, 403)

# Admin Authorization
@api_view(['GET'])
@permission_classes([IsAdminUser])
def admins(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        admins = Group.objects.get(name="Admin")
        admins.user_set.add(user)
        return Response({'message': 'Hi Admin!'})
    
    return Response({'message': 'Error'}, status.HTTP_400_BAD_REQUEST)

# Throttling -------------------------------------------------------------------------------------------------------------

# Unauthenticated users throttling
@api_view(['GET'])
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message': 'successful'})

# Authenticated users throttling
@api_view(['GET'])
@throttle_classes([UserRateThrottle])
@permission_classes([IsAuthenticated])
def throttle_check_auth(request):
    return Response({'message': 'successful: This message will apear for logged users only'})

# Custom throttling 
"""
Let's say we want to let the authenticated users to access an API endpoint 20 times but in settings.py 'user': '10/minute' this is the general
rule. So we need to defiend a custom throttle class. We can see this in the following function

"""
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@throttle_classes([TwentyCallsPerMinute])
def throttle_check_auth_twenty(request):
    return Response({'message': 'successful: This message will apear for logged users only'})