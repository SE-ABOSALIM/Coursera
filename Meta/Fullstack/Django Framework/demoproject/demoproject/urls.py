from django.contrib import admin 
from django.urls import path, include
from django.http import HttpResponse
from app import views

urlpatterns = [ 
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('demo/', views.index, name='index'), # name='index' alias for demo page
    path('app2/', include('app2.urls')), # return HttpResponse & implement urls.py in app level
    path('app3/', include('app3.urls')), # Multiple url paths with multiple view functions
    path('app4/', include('app4.urls')), # Display Http Request meta data
    path('app5/', include('app5.urls')), # Url Query Parameters
    path('app6/', include('app6.urls')), # Url Parameters
    path('app7/', include('app7.urls')), # namespace to differentiate between app pages 
    path('app8/', include('app8.urls')), # namespace to differentiate between app pages 
    path('app9/', include('app9.urls')), # Empty app (maybe practice something with it)
    path('app10/', include('app10.urls')), # models, migrations & admin panel registration
    path('app11/', include('app11.urls')), # models with ForeignKey practice
    path('app12/', include('app12.urls')), # models excersize to practice creating forms
    path('app13/', include('app13.urls')), # Templates
]

# DEBUG = False Required
handler404 = 'demoproject.views.handler404'
handler400 = 'demoproject.views.handler400'