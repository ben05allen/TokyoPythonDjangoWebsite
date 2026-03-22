from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time_start = models.TimeField(blank=True, null=True)
    time_end = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=300, blank=True)
    link = models.URLField(blank=True)
    link_label = models.CharField(max_length=100, default="RSVP")
    is_upcoming = models.BooleanField(default=True)
    color = models.CharField(
        max_length=20,
        choices=[("primary", "Red"), ("secondary", "Blue")],
        default="primary",
    )

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.title} ({self.date})"

    @property
    def month_label(self):
        return self.date.strftime("%B %Y")

    @property
    def short_month(self):
        return self.date.strftime("%b").upper()

    @property
    def day(self):
        return self.date.day


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField()
    content = models.TextField(blank=True)
    published_date = models.DateField(default=timezone.now)
    link = models.URLField(blank=True)

    class Meta:
        ordering = ["-published_date"]

    def __str__(self):
        return self.title

    @property
    def month_label(self):
        return self.published_date.strftime("%B %Y")


class CalendarEvent(Event):
    """Proxy model for managing events shown on the calendar page."""

    class Meta:
        proxy = True
        verbose_name = "Calendar Event"
        verbose_name_plural = "Calendar Events"


class GameSession(models.Model):
    player_hp = models.IntegerField(default=100)
    player_attack = models.IntegerField(default=10)
    player_level = models.IntegerField(default=1)
    player_x = models.IntegerField(default=0)
    player_y = models.IntegerField(default=0)
    map_data = models.JSONField(default=dict)
    log = models.JSONField(default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    game_id = models.DateTimeField(auto_now_add=True)
