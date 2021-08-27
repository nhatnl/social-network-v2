from django.shortcuts import get_object_or_404

from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
        Permission Class For Owner of a post Or Admin
    """
    def has_permission(self, request, view):
        keyword = view.lookup_url_kwarg
        object = get_object_or_404(view.model,id=view.kwargs[keyword])
        user = request.user
        if object.user == user or user.is_superuser:
            return True
        else:
            return False