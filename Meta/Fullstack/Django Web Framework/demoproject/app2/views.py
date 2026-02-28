from django.http import HttpResponse

# Create your views here.
def index(req):
    content = '<html><head></head><body> <h1>Hello Django, From app2</h1> <h2>urls.py is used in this app</h2> </body></html>'
    return HttpResponse(content)