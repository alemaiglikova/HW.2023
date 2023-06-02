from django.urls import path
from django_app import views

urlpatterns = [
    #    url     func                   name (уникальная ссылка на этот маршрут)
    path('', views.home),


]