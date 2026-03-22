from django.contrib import admin
from .models import Event, BlogPost, CalendarEvent


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_upcoming", "location")
    list_filter = ("is_upcoming", "color")
    list_editable = ("is_upcoming",)
    ordering = ("-date",)


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "time_start", "time_end", "location", "color", "is_upcoming")
    list_filter = ("color", "is_upcoming", "date")
    list_editable = ("time_start", "time_end", "color", "is_upcoming")
    ordering = ("date", "time_start")
    date_hierarchy = "date"
    search_fields = ("title", "location", "description")
    fieldsets = (
        (None, {
            "fields": ("title", "description"),
        }),
        ("Schedule", {
            "fields": ("date", "time_start", "time_end"),
        }),
        ("Details", {
            "fields": ("location", "link", "link_label", "color", "is_upcoming"),
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    ordering = ("-published_date",)
