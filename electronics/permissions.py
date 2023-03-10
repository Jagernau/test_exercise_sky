from rest_framework import permissions


class ActivePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active == True:
            return True
        else:
            return False
