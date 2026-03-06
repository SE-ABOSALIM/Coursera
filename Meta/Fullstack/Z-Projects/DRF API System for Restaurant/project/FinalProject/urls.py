from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items, name='menu-items'),
    path('menu-items/<int:pk>', views.menu_item_details, name='menu-items-detail'),

    path('orders', views.orders),
    path('orders/<int:id>', views.order_details),
    path('cart/menu-items', views.user_cart),

    path('groups/<str:group_name>/users', views.group_users),
    path('groups/<str:group_name>/users/<int:id>', views.group_user_detail),
]