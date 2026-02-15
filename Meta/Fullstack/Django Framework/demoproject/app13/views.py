from django.shortcuts import render

def about(request):
    about_context = {
        "about_us": "We are software engineers, working on creating end-to-end web applications. We aim to be senior engineers and gain a lot of experience.",
        "items": [
            {"name": "Ali", "surname": "Abdullah"},
            {"name": "Ahmed", "surname": "Muhammed"},
        ],
    }
    return render(request, "about.html", about_context)
