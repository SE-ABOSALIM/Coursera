from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('BookListAPI.urls')), # API request handling (GET, POST)
    path('debug/', include('DebugExample.urls')), # API request handling (GET, POST)
]