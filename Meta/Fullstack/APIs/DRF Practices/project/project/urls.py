from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include('BookListAPI.urls')), 
    path('api/', include('SimpleAPIPractice.urls')), # serializers with helper APIView and class-based views, simple API Project
    path('api/', include('Serialization.urls')), # Filtering | Ordering | Searching | Pagination and validators
    path('api/', include('APISecurity.urls')), # 
]