from django.db.models import Q, F
from .models import Tag


def get_user_tags(user_id: int):
    user_id_field = F("notes__user_id")
    queryset = Tag.objects.select_related("notes").filter(Q(notes__user_id=user_id)).values('content')

    return queryset
