import calendar as cal
from datetime import date, timedelta

from django.shortcuts import render
from .models import Event, BlogPost, CalendarEvent


def home(request):
    upcoming_events = Event.objects.filter(is_upcoming=True)[:2]
    return render(request, "home/index.html", {"upcoming_events": upcoming_events})


def about(request):
    return render(request, "home/about.html")


def calendar(request):
    today = date.today()
    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))

    # Clamp values
    if month < 1:
        month, year = 12, year - 1
    elif month > 12:
        month, year = 1, year + 1

    # Previous / next month for nav links
    prev_month = date(year, month, 1) - timedelta(days=1)
    if month == 12:
        next_month = date(year + 1, 1, 1)
    else:
        next_month = date(year, month + 1, 1)

    # Build weeks grid (Mon=0)
    cal_obj = cal.Calendar(firstweekday=0)
    weeks = cal_obj.monthdatescalendar(year, month)

    # Fetch events for the visible date range
    first_day = weeks[0][0]
    last_day = weeks[-1][-1]
    events_qs = CalendarEvent.objects.filter(date__gte=first_day, date__lte=last_day)

    # Map events by date
    events_by_date = {}
    for event in events_qs:
        events_by_date.setdefault(event.date, []).append(event)

    # Build template-friendly structure
    calendar_weeks = []
    for week in weeks:
        days = []
        for d in week:
            days.append({
                "date": d,
                "day": d.day,
                "in_month": d.month == month,
                "is_today": d == today,
                "events": events_by_date.get(d, []),
            })
        calendar_weeks.append(days)

    month_label = date(year, month, 1).strftime("%B")
    year_label = year

    # Sidebar data
    upcoming_events = CalendarEvent.objects.filter(is_upcoming=True)[:5]
    past_events = CalendarEvent.objects.filter(is_upcoming=False).order_by("-date")

    # Today's events for the side panel
    today_events = CalendarEvent.objects.filter(date=today)

    return render(request, "home/calendar.html", {
        "calendar_weeks": calendar_weeks,
        "month_label": month_label,
        "year_label": year_label,
        "today": today,
        "prev_month": prev_month,
        "next_month": next_month,
        "upcoming_events": upcoming_events,
        "past_events": past_events,
        "today_events": today_events,
    })


def blog(request):
    posts = BlogPost.objects.all()
    return render(request, "home/blog.html", {"posts": posts})
