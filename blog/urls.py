from django.urls import path

from . import views
from .views import post_list

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('author/<int:author_id>/posts/', views.posts_by_author, name='posts_by_author'),
]
