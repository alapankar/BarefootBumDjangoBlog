from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home , name='blog-home'),
    path('register/', user_views.register, name='blog-register'),
    path('about/', views.about , name='blog-about'),
]