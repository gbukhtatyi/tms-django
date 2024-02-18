from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListCreateAPIView.as_view(), name="api-events"),
    path("/my", views.MyEventsListView.as_view()),
    path("/<event_id>", views.SubscribeView.as_view())
]
