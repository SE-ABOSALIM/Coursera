from django.http import HttpResponse

# Create your views here.
def home(req):
    content = """ <h1 style="color: #00179C;"> This is main page from main app </h1> """
    return HttpResponse(content)