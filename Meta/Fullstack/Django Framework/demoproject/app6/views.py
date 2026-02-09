from django.http import HttpResponse

def show_colors(request, color):
    colors = {
        'green': 'My favorite color',
        'black': 'The color of the shadow',
        'white': 'Peacful and great color'
    }

    try:
        description = colors[color]
    except:
        return HttpResponse("Requested color doesn't exist")
    
    return HttpResponse(f"<h2> {color} </h2>" + description)
