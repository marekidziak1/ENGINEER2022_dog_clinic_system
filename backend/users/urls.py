from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.registerView, name='register_user'),
    path('login/', views.loginView, name='login_user'),
]