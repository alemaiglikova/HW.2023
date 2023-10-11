from drf_yasg.generators import OpenAPISchemaGenerator

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)

        return schema

from rest_framework.authentication import BaseAuthentication

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
    
        return None

from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    def has_permission(self, request, view):

        return True
