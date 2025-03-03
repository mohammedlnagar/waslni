from django.urls import path
from .views import register, user_login, user_logout, profile, edit_profile, validate_registration
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('validate-registration/', validate_registration, name='validate_registration'),

]
