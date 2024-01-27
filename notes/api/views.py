import uuid

from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from notes.api.permissions import IsOwnerOrReadOnly
# Api
from notes.api.serializers import NoteSerializer, NoteListSerializer, TagSerializer, TagListSerializer
# Notes
from notes.models import Note, Tag


class NoteListCreateAPIView(ListCreateAPIView):
    queryset = Note.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return NoteSerializer
        return NoteListSerializer

    def perform_create(self, serializer):
        """Во время создания рецепта добавляем владельца"""
        serializer.save(user=self.request.user)


class NoteDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = 'uuid'
    lookup_url_kwarg = 'note_uuid'
    permission_classes = [IsOwnerOrReadOnly]


class TagListCreateAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TagSerializer
        return TagListSerializer


def api_notes_index(request):
    return Response(dict(zip(Note.objects.all())))


def api_notes_view(request, note_uuid):
    print(note_uuid)
    note = get_object_or_404(Note, uuid=uuid.UUID(note_uuid))
    return NoteSerializer(data=note)


def api_tags_index(request):
    return Response(dict(zip(Tag.objects.all())))
