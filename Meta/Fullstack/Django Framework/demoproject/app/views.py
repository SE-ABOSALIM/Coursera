from django.http import HttpResponse

# Create your views here.
def index(req):
    content = '<html><head></head><body> <h1>This is the main page from app</h1> </body></html>'
    return HttpResponse(content)