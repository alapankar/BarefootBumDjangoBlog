from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home , name='blog-home'),
    path('register/', user_views.register, name='blog-register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='blog-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='blog-logout'),
    path('about/', views.about , name='blog-about'),
]