from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news_list, name='news_list'),
    path('categories/', views.category_list, name='category_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]
