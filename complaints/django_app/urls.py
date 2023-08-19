from django.urls import path
from .views import feedback_view, feedback_success_view

urlpatterns = [
    path('feedback/', feedback_view, name='feedback'),
    path('feedback/success/', feedback_success_view, name='feedback_success'),
]