from django.urls import path
from . import views

urlpatterns = [
    path("", views.RegisterApiView.as_view(), name="api-users"),
]
