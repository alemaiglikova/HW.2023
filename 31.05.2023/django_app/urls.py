from django.urls import path
from django_app import views
urlpatterns = [
    #    url     func                   name
    path('', views.home, name="home"),

]