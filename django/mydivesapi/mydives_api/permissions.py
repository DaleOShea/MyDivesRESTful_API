from rest_framework import permissions


# Ref Point: http://www.django-rest-framework.org/api-guide/permissions/#custom-permissions

class allowAccessToUserOwnContent(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True

            return obj.id == request.user.id
