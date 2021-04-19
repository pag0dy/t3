from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('editarperfil', views.editarperfil, name='editarperfil'),
    path('editarpass', views.editarpass, name='editarpass'),
    path('companyprofile', views.companyprofile, name='companyprofile'),
    path('editcompany', views.editcompany, name='editcompany'),
    path('staff_info/<int:id>', views.staff_info, name='staff_info'),
    path('editstaff/<int:id>', views.editstaff, name='editstaff'),
    path('deletestaff', views.deletestaff, name='deletestaff')
]