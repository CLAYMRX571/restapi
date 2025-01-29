from rest_framework.permissions import BasePermission
from datetime import datetime

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsAdminOrEditor(BasePermission):
    def has_permission(self, request, view):
        return request.user and (
            request.user.is_staff or request.user.groups.filter(name='editors').exists()
        )

class IsWorkingHours(BasePermission):
    def has_permission(self, request, view):
        current_hour = datetime.now().hour()
        return 9 <= current_hour < 18