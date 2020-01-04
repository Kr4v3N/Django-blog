from django.urls import path

from pyblog import views

urlpatterns = [
    path('posts/', views.post_list, name='home'),
]