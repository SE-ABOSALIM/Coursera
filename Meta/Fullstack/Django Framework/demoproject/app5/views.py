from django.http import HttpResponse

# URL Query Parameters
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    product_number = request.GET['product_number']

    # URL: http://localhost:8000/app5/getuser/?name=Ali&id=10&product_number=13
    return HttpResponse("Name: {}<br>UserID: {}<br>Product Number: {}<br> These values are coming from url query parameters".format(name, id, product_number)) 