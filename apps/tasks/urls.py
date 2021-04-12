from django.urls import path
from . import views

urlpatterns = [
    path('createProject', views.createProject, name='createProject'),
    path('project/<int:id>', views.project, name='project'),
    path('addTask', views.addTask, name='addTask')
]