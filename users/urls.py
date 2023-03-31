from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('signup/', views.signUpView, name='signup'),
    path('profile/', views.profileView, name='profile'),
    path('', views.homeView, name='home'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)