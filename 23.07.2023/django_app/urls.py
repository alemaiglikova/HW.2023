from django.urls import path
from . import views

app_name = 'your_app'

urlpatterns = [
    path('registration/', views.registration_view, name='registration'),

]
