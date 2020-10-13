from django.db import models

from room.models import Room, Location, Player


class World(models.Model):
    """
    The class is a representation of the world created from a room.
    Keeps data about objects set up by users.
    Having related world determines if game is on or not.
    """
    room = models.OneToOneField(Room, on_delete=models.CASCADE)


class GameObject(models.Model):
    """
    Objects placed by players and stuff generated.
    Name identifies which model etc. should be used on the client side.
    """
    name = models.TextField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='game_objects')
    created_by = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True,
                                   help_text="If null then game object was automatically generated.",
                                   related_name='game_objects')
