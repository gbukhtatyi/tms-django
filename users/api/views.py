from django.http import Http404
from rest_framework.generics import ListCreateAPIView
from .permissions import IsSuperUser
from .serializers import RegisterSerializer
from users.models import User


class RegisterApiView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsSuperUser]

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser is False:
            raise Http404

        return self.list(request, *args, **kwargs)
