from django.urls import path
from . import views

urlpatterns = [
    path('createProject', views.createProject, name='createProject')
]