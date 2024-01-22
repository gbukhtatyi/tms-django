from rest_framework.response import Response
# Notes
from notes.models import Note


def api_notes_index():
    notes = Note.objects.all()

    return Response({})


def api_notes_view():
    return Response({})
