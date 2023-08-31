from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all_posts'), 
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
    path('register/', views.registration_view, name='registration'),

]
