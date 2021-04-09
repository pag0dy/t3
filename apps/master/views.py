from django.shortcuts import render, redirect, HttpResponse
from ..users.forms import RegistrationForm, LoginForm
from ..users.models import User, Company
from .utils import filtro_usuario, filtro_usuario_email

def crearSesion(request, usuario):
    request.session['id'] = usuario.id
    print('Sesión creada')
    return True

def home(request):
    return render(request, 'home.html')


def login(request):
    if 'id' in request.session:
        del request.session['id']
        return render(request, 'login.html')  
    else:
        return render(request, 'login.html')    

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nuevo_usuario = form.save(commit=False)
            password = form.clean_password()
            
            if password:
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
                nuevo_usuario.password = pw_hash
                nuevo_usuario.save()
                crearSesion(request, nuevo_usuario)
                return redirect('review/home')

        else:                    
            return redirec('register')

    else:
        form = RegistrationForm()
        context = {
            'reg_form' : form,
        }
        return render(request, 'register.html', context)

def index(request):
    return render(request, 'index.html')

def logout(request):
    return HttpResponse('Salir')

def worksesh(request):
    return render(request, 'worksesh.html')