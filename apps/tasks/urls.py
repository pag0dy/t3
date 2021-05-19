from django.urls import path
from . import views

urlpatterns = [
    path('createProject', views.createProject, name='createProject'),
    path('project/<int:id>', views.project, name='project'),
    path('project/edit/<int:id>', views.editProject, name='editProject'),
    path('project/remove/<int:id>', views.removeProject, name='removeProject'),
    path('addTask', views.addTask, name='addTask'),
]