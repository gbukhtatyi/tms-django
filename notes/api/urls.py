from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path("/tags", views.TagListCreateAPIView.as_view(), name="api-tags"),

    path("/", views.NoteListCreateAPIView.as_view(), name="api-notes"),
    path("/<note_uuid>", views.NoteDetailAPIView.as_view(), name="aoi-notes-view"),
]
