from rest_framework.permissions import BasePermission


class PostOrIsSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method in ('POST')
            or request.user.is_superuser
        )
