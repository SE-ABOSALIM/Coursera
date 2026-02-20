from rest_framework import generics
from .models import Cars
from .serializers import CarsSerializers

class CarsListCreateView(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializers

class CarDetailView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView): # allows you to update(PUT/PATCH), display(GET) and remove(DELETE) 
    queryset = Cars.objects.all()
    serializer_class = CarsSerializers