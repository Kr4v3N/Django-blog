from django.urls import path

from pyblog import views

urlpatterns = [
    path('posts/', views.post_list, name='home'),
    path('posts/<str:category_name>/', views.post_list, name='post-list'),
    path('posts/detail/<int:post_id>/', views.post_detail, name='post-detail'),
]