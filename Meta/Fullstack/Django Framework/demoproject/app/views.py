from django.http import HttpResponse 

def index(request):
    content = '<html><head></head><body> <h1>Hello Django, From app</h1> <h2>urls.py is NOT used in this app</h2> </body></html>'
    return HttpResponse(content)