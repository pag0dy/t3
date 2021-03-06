from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('registersolo', views.registersolo, name='registersolo'),
    path('worksesh', views.worksesh, name='worksesh'),
    path('startworksesh', views.startworksesh, name='startworksesh'),
    path('stopworksesh', views.stopworksesh, name='stopworksesh'),
    path('logout', views.logout, name='logout'),
    path('team_setup', views.team_setup, name='team_setup'),
    path('manage_team', views.manage_team, name='manage_team'),
    path('report', views.report, name='report')
]