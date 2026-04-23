from django.shortcuts import render


# Create your views here.
def move(request, direction):
    context = {
        "title": "Welcome!",
        "message": "This is my Django homepage.",
    }
    return render(request, "home/index.html", context)
