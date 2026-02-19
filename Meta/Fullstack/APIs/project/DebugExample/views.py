from django.http import HttpResponse

def view_even_numbers(request):
    response = ''
    numbers = [1,2,3,4,5,6,7,8,9]

    for i in numbers:
        if i % 2 == 0:
            response += str(i) + ", "

    return HttpResponse(response)