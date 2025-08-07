from django.urls import path 
from django.contrib.auth import views as auth_views
from authentication import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('change-username/', views.change_username, name='change_username'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/password_change_form.html',
        success_url='/'
    ), name='password_change'),
    path('delete-account/', views.delete_account, name='delete_account'),
]

