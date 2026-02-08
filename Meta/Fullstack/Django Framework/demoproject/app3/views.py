from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(req):
    content = """ <h1 style="color: #00179C;"> Hello From app3 home page </h1> """
    return HttpResponse(content)

def greet(req):
    content = """ <h1 style="color: #00179C;"> Hello Brother, This is greet page in app3 </h1> """
    return HttpResponse(content)

def display_year(req):
    year = datetime.today().year
    content = f"""<h1 style="color: #00179C;"> We are in {year}, Btw this is display_year page in app3 </h1>"""
    return HttpResponse(content)