from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Права доступа автору или авторизованному пользователю."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and obj.author == request.user
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Права доступа только для администратора"""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS or request.user.is_staff
        )
