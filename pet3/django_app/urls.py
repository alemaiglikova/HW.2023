
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView, NewsListCreateView, NewsRetrieveUpdateDestroyView, ComplaintListCreateView, ComplaintRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
    path('news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroyView.as_view(), name='news-retrieve-update-destroy'),
    path('complaints/', ComplaintListCreateView.as_view(), name='complaint-list-create'),
    path('complaints/<int:pk>/', ComplaintRetrieveUpdateDestroyView.as_view(), name='complaint-retrieve-update-destroy'),
]

