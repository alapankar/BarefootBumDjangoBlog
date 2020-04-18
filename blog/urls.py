from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/new/', PostCreateView.as_view() , name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
    path('register/', user_views.register, name='blog-register'),
    path('profile/', user_views.profile, name='blog-profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='blog-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'), name='blog-logout'),
    path('about/', views.about , name='blog-about'),
]