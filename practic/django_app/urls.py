# urls.py
from django.urls import path

from . import views
from .views import post_list, post_detail, create_post, add_comment, comment_list, login_user, register_user, \
    user_detail, user_list

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>/', user_detail, name='user_detail'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/comments/', views.comment_list, name='comment_list'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    # Другие маршруты, если необходимо
]
