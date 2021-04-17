from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('editarperfil', views.editarperfil, name='editarperfil'),
    path('companyprofile', views.companyprofile, name='companyprofile'),
    path('staff_info/<int:id>', views.staff_info, name='staff_info')
]