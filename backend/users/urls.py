from . import views
from .forms import UserPasswordResetForm #,UserPasswordChangeForm
from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [
    path('register/', views.registerUser, name='register_user'),
    path('login/', views.loginUser, name='login_user'),
    path('logout/', views.logoutUser, name='logout_user'),
    path('profile/', views.updateProfile, name='update_profile'),
    path('reset_password/',auth_views.PasswordResetView.as_view(
            template_name="users/password_reset.html", form_class=UserPasswordResetForm),
            name="reset_password"),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"), 
            name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"),#, form_class = UserPasswordChangeForm), 
            name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"),  
            name="password_reset_complete"),
]