from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm, LoginForm
from .models import User, Company
from ..master.utils import filtro_usuario_email, filtro_usuario

def user(request):
    return HttpResponse('Inicio')


