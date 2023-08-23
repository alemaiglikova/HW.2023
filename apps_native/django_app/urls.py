from django.urls import path
from . import views

urlpatterns = [
    path('submit-idea/', views.submit_idea_view, name='submit_idea'),
    path('ideas-list/', views.ideas_list_view, name='ideas_list'),
]
