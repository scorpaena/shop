from rest_framework import permissions


class IsEditor(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name='editors').exists()

    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='editors').exists()