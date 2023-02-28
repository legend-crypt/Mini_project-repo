from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('signup/', views.signUpView, name='singup'),
    path('profile', views.profileView, name='profile'),
    path('', views.homeView, name='home'),

]
