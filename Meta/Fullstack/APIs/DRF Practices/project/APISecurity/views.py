from rest_framework.decorators import ( 
    api_view, 
    permission_classes, 
    throttle_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TwentyCallsPerMinute

# Authentication and Authorization ----------------------------------------------------------------------------------------

# Authentication
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # If we don't provide the credentials it will give us a 401-Unauthorized response
def secret(request):
    return Response({'message': 'Some secret message'})

# Authorization
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({'message': 'Only manager should see this message'})
    else:
        return Response({'message': 'Authorization required for this area'}, 403)
    
# ------------------------------------------------------------------------------------------------------------------------



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