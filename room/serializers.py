from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from room.models import Room, Player, Location


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

    def validate(self, attrs):
        # When creating new player aka joining the room
        if not self.instance:
            if not attrs.get('room_id'):
                raise ValidationError("Provide room id.")
            else:
                try:
                    room = Room.objects.get(id=attrs.get('room_id'))
                    if Player.objects.filter(team__room=room).count() >= room.max_players:
                        raise ValidationError("Room is full.")
                except Room.DoesNotExist:
                    raise ValidationError("Room not found.")
        return attrs

    def create(self, validated_data):
        instance = super().create(validated_data)
        # Add empty location object (don't get players location when in a Lobby
        location = Location.objects.create()
        instance.location = location
        instance.save()
        return instance


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
