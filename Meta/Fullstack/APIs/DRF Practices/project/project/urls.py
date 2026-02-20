from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include('BookListAPI.urls')), 
    path('api/', include('SimpleAPIPractice.urls')), # serializers, simple API Project
]
