from django.contrib import admin
from .models import Event, BlogPost


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_upcoming", "location")
    list_filter = ("is_upcoming", "color")
    list_editable = ("is_upcoming",)
    ordering = ("-date",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    ordering = ("-published_date",)
