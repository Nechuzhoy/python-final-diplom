from rest_framework import permissions


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
       # чтение всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Правка владелец
        return obj.id == request.user.id





