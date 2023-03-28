from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('photo/upload/', views.photo_upload, name="photo_upload"),
    path('blog/create', views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:blog_id>', views.view_blog, name='view_blog'),
    path('blog/<int:blog_id>/edit', views.edit_blog, name='edit_blog')
]
