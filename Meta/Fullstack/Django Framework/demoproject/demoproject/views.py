from django.http import HttpResponse

# DEBUG = False Required
def handler404(request, exception):
    return HttpResponse(
        """
        <h1>404: Page Not Found</h1>
        <button onclick="window.location.href='/'">
            Go to Homepage
        </button>
        """,
        status=404
    )

def handler400(request, exception):
    return(HttpResponse("<h1>400: Bad Request!</h1>"))