from django.shortcuts import render, redirect, HttpResponse

def home(request):
    return render(request, 'home.html')

def login(request):
    return HttpResponse('Iniciar sesión')

def register(request):
    return HttpResponse('Registrate')

def logout(request):
    return HttpResponse('Salir')

def index(request):
    return render(request, 'index.html')

def worksesh(request):
    return render(request, 'worksesh.html')