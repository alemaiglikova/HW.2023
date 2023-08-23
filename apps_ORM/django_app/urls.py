from django.urls import path
from . import views

urlpatterns = [
    path('submit_idea/', views.submit_idea, name='submit_idea'),
    path('ideas_list/', views.ideas_list, name='ideas_list'),
]
