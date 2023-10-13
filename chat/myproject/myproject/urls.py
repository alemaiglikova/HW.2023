"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from utils import CustomSchemaGenerator, CustomAuthentication, CustomPermission

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from datetime import timedelta

advanced_schema_view = get_schema_view(
    openapi.Info(
        title="Advanced API",
        default_version='v1',
        description="Advanced API with additional features",
        terms_of_service="https://www.myapp.com/terms/",
        contact=openapi.Contact(email="contact@myapp.com"),
        license=openapi.License(name="Custom License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=CustomSchemaGenerator,  # Подставьте свой собственный класс генератора
    authentication_classes=(CustomAuthentication,),  # Подставьте свой собственный класс аутентификации
    permission_classes=(CustomPermission,),  # Подставьте свой собственный класс разрешений
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('myapp.urls')),


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    path('swagger/advanced/', advanced_schema_view.with_ui('swagger', cache_timeout=0, config_name='advanced'), name='schema-advanced-swagger-ui'),
    path('redoc/advanced/', advanced_schema_view.with_ui('redoc', cache_timeout=0, config_name='advanced'), name='schema-advanced-redoc'),
]


CELERY_BEAT_SCHEDULE = {
    'periodic_task': {
        'task': 'myapp.tasks.periodic_task',
        'schedule': timedelta(minutes=30), 
    },
}

