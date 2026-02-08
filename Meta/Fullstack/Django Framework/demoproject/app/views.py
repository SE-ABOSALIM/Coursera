from django.http import HttpResponse 

def index(request):
    content = '<html><head></head><body> <h1>I am Learning Django</h1> </body></html>'
    return HttpResponse(content)