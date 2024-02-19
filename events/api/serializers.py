from rest_framework import serializers
from rest_framework.fields import DateTimeField

from events.models import Event
from users.api.serializers import UserSerializer


class EventSerializer(serializers.ModelSerializer):
    meeting_time = DateTimeField()
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'description', 'meeting_time', 'users']
        read_only_fields = ["id"]


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
