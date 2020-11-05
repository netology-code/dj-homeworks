from rest_framework import permissions


class isAllowed(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            current_object = view.queryset.filter(id=view.kwargs['pk'])[0]
            if current_object.creator_id == request.user.id:
                return True

