from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.user == obj.creator


class IsOwnerDraft(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in [*permissions.SAFE_METHODS, 'POST'] and not obj.draft:
            return True
        return obj.draft and obj.creator == request.user
