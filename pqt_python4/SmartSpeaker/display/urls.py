from django.urls import path
from . import views

app_name = 'display'

urlpatterns = [
    path('messages/', views.display_messages, name='display_messages'),
]
