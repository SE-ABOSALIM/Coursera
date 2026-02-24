from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path
from . import views

urlpatterns = [
    # Authentication and Authorization ----------------------------------------------------------------------------------------
    path('secret', views.secret),
    path('manager-view', views.manager_view),
    path('admin-view', views.admins),
    path('token-auth', obtain_auth_token),

    # Throttling --------------------------------------------------------------------------------------------------------------
    path('throttle-check', views.throttle_check),
    path('throttle-check-auth', views.throttle_check_auth),
    path('throttle-check-auth-twenty', views.throttle_check_auth_twenty),
]