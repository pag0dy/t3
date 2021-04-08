from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('worksesh', views.worksesh, name='worksesh'),
    path('logout', views.logout, name='logout')
]