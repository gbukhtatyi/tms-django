from django.contrib.auth import get_user_model
from rest_framework import serializers

from notes.models import Note, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'content']


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'content']


class NoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        slug_field='content'
    )

    class Meta:
        model = Note
        fields = ["uuid", "title", "content", "image", "tags", "user"]


class NoteListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='content'
    )

    class Meta:
        model = Note
        fields = ["uuid", "title", "image", "tags", "user", "created_at"]
