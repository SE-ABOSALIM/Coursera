from django.urls import path
from . import views

urlpatterns = [
    path('foods/', views.foods_menu),
    path('foods/<int:pk>', views.foods_menu_item),
    path('foods-filtered', views.foods_menu_filtered),
    path('foods-filtered/<int:pk>', views.foods_menu_item_filtered),

    # ----------------------------------------------------------------------------------

    path('menu-items', views.menu_items),
    path('menu-items/<int:pk>', views.single_menu_item),
    path('category/<int:pk>', views.category_detail, name='category-detail')
]