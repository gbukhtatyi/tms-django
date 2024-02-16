from django.db.models import Q, F
from .models import Tag


def get_user_tags(user_id: int):
    return Tag.objects.filter(notes__user__id=user_id).values_list("content", flat=True).distinct()
