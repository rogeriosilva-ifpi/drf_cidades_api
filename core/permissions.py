from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        # TODO
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):

        if (request.method in permissions.SAFE_METHODS):
            return True

        # TODO (owner is auth-user)
        return True
