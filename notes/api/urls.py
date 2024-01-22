from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path("", views.api_notes_index, name="api-notes"),
    path("<id>", views.api_notes_view, name="aoi-notes-view")
]
