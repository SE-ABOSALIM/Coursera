from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items, name='menu-items'),
    path('menu-items/<int:pk>', views.single_menu_items, name='menu-items-detail'),

    # path('orders'),
    # path('orders/<int:id>'),

    # path('groups/<str:group_name>/users'),
    # path('groups/<str:group_name>/users/<int:id>'),
    # path('cart/menu-items'),
]