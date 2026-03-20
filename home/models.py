from django.db import models


# Create your models here.
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
