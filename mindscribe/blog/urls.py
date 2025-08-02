from django.urls import path, include
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.blog_list, name='home'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('blog/edit/<int:blog_id>/', views.blog_edit, name='blog_edit'),
    path('blog/delete/<int:blog_id>/', views.blog_delete, name='blog_delete'),
    
    path('register/', views.register, name='register'),
    
]