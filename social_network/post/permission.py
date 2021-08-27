from rest_framework.permissions import BasePermission

class ObjectIsAccessible(BasePermission):
    """
        Check if a post is open for access
    """

    def has_object_permission(self, request, view, obj):
        if obj.mode == 'PR' and obj.user is not request.user:
            return False
        else:
            return True
    
    def has_permission(self, request, view):
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)
    
