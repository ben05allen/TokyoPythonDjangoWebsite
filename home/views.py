from django.shortcuts import render
from .models import Event, BlogPost


def home(request):
    upcoming_events = Event.objects.filter(is_upcoming=True)[:2]
    return render(request, "home/index.html", {"upcoming_events": upcoming_events})


def about(request):
    return render(request, "home/about.html")


def calendar(request):
    upcoming_events = Event.objects.filter(is_upcoming=True)
    past_events = Event.objects.filter(is_upcoming=False).order_by("-date")
    return render(request, "home/calendar.html", {
        "upcoming_events": upcoming_events,
        "past_events": past_events,
    })


def blog(request):
    posts = BlogPost.objects.all()
    return render(request, "home/blog.html", {"posts": posts})
