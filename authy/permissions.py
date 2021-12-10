from rest_framework import permissions


class UserPermission(permissions.BasePermission):
   message = "You do not have the permission to perform this action."

   def has_permission(self, request, view):
      return True

   def has_obj_permission(self, request, view, obj):
      return True
