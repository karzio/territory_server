from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from room.models import Room
from world.models import World, GameObject


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = '__all__'

    def validate(self, attrs):
        # When creating new world aka starting the game
        if not self.instance:
            if not attrs.get('room_id'):
                raise ValidationError("Provide room id.")
            else:
                try:
                    room = Room.objects.get(id=attrs.get('room_id'))
                    if room.world:
                        raise ValidationError("Game already started.")
                except Room.DoesNotExist:
                    raise ValidationError("Room not found.")
        return attrs


class GameObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameObject
        fields = '__all__'

    def validate(self, attrs):
        if not self.instance:
            world_id = attrs.get('world_id')
            player_id = self.context.get('player_id')
            if not world_id:
                raise ValidationError("Provide world id.")
            try:
                World.objects.get(Q(room__team_one__player__id=player_id)
                                  | Q(room__team_two__player_id=player_id),
                                  id=world_id)
            except World.DoesNotExist:
                raise ValidationError("Player does not exist in this world.")
        return attrs
