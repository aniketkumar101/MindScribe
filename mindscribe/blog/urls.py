from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.blog_create, name='blog_create'),
    path('edit/<int:blog_id>/', views.blog_edit, name='blog_edit'),
    path('delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    
    path('register/', views.register, name='register'),
    
]