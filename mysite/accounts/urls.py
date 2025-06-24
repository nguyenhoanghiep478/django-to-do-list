from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView,ProfileView


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts/login.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
]