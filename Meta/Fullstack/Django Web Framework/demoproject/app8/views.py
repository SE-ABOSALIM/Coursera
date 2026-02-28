from django.http import HttpResponse

def auth_login(request):
    return HttpResponse('Login Successful from app8')