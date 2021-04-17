from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, LoginForm, EditUserForm
from .models import User, Company
from ..tasks.models import Task, Assignments, Project
from ..master.utils import filtro_usuario_email, filtro_usuario, filtro_empresa

def user(request):
    this_user = filtro_usuario(request.session['id'])
    return render(request, 'mi_info.html', {'user':this_user})


def editarperfil(request):
    this_user = filtro_usuario(request.session['id'])
    if request.method == 'GET':
        editform = EditUserForm()
        return render(request, 'editarperfil.html', {'editform':editform})
    else:
        return Http('editar perfil')

def companyprofile(request):
    this_user = filtro_usuario(request.session['id'])
    company = filtro_empresa(request.session['company'])
    context = {
        'user':this_user,
        'company':company
    }
    return render(request, 'company.html', context)

def staff_info(request, id):
    this_user = filtro_usuario(request.session['id'])
    company = filtro_empresa(request.session['company'])
    staff = filtro_usuario(id)
    context = {
        'user':this_user,
        'company':company,
        'staff':staff
    }
    return render(request, 'staff_info.html', context)