from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from world.models import World, GameObject
from world.serializers import WorldSerializer, GameObjectSerializer


class WorldViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer


class GameObjectViewSet(ModelViewSet):
    queryset = GameObject.objects.all()
    serializer_class = GameObjectSerializer
