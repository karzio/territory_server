from django.db import models


class Location(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)


class Room(models.Model):
    name = models.TextField(default='Game room')
    max_players = models.IntegerField(default=10)


class Team(models.Model):
    name = models.TextField(default='Team name')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='teams')


class Player(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='players')

