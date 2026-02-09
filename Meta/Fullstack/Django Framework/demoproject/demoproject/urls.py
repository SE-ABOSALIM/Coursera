from django.contrib import admin 
from django.urls import path, include
from django.http import HttpResponse
from app import views

urlpatterns = [ 
    path('', include('main.urls')),
    path('demo/', views.index, name='index'), # name='index' alias for demo page
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('app4/', include('app4.urls')),
    path('app5/', include('app5.urls')),
    path('app6/', include('app6.urls')),
    path('app7/', include('app7.urls')),
    path('app8/', include('app8.urls')),
    path('app9/', include('app9.urls')),
]