from django.urls import path
from . import views
app_name = "app8" # To differentiate between app7 and app8 login pages we use this namespace

"""
Execute this command to test in the terminal

python manage.py shell
from django.urls import reverse
reverse("app8:login")

Now examine the output
"""

# Same page name with app7.views
urlpatterns = [
    path('login/', views.auth_login, name='login')
]