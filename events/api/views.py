from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from events.models import Event
from .serializers import EventSerializer


class EventListCreateAPIView(ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = Event.objects.all()  # .filter(meeting_time__gt=datetime.now())

    def get_serializer_class(self):
        current_user = self.request.user

        if current_user.is_superuser is False:
            raise Http404

        return EventSerializer


class MyEventsListView(ListAPIView):
    def get_queryset(self):
        current_user = self.request.user

        return Event.objects.filter(users__in=[current_user])

    def get_serializer_class(self):
        return EventSerializer


class SubscribeView(APIView):
    permission_classes = [IsAuthenticated]

    @csrf_exempt
    def post(self, request, event_id,format=None):
        current_user = request.user

        event = get_object_or_404(Event, id=event_id)
        event.users.add(current_user)
        event.save()

        return Response(EventSerializer(event).data)


