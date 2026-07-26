from rest_framework.permissions import BasePermission

# 
class IsBibliothecaireOuAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role in ['bibliothecaire','admin']


class IsAdmin(BasePermission):
    def has_permission(self,request,view):
        return request.user.is_authenticated and request.user.role=='admin'
    