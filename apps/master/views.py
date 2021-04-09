from django.shortcuts import render, redirect, HttpResponse
from ..users.forms import RegistrationForm, LoginForm
from ..users.models import User, Company
from .utils import filtro_usuario, filtro_usuario_email
import bcrypt

def crearSesion(request, usuario):
    request.session['id'] = usuario.id
    print('Sesión creada')
    return True

NoCompany = Company.objects.get(id=1)

def home(request):
    if 'id' in request.session:
        this_user = filtro_usuario(request.session['id'])
    return render(request, 'home.html', {'user':this_user})


def login(request):
    if request.method == 'POST':
        errors = User.objects.validar_inicio(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('login')
        
        else:
            este_usuario = filtro_usuario_email(request.POST['email'])
            crearSesion(request, este_usuario)
            return redirect('home')

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
                if nuevo_usuario.account_type == 'SU':
                    nuevo_usuario.company = NoCompany
                    nuevo_usuario.save()
                    crearSesion(request, nuevo_usuario)
                    return redirect('home')
                else:
                    crearSesion(request, nuevo_usuario)
                    return redirect('team_setup')

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
    try:
        del request.session['id']
        return redirect('index')
    except:
        return HttpResponse('no has iniciado una sesión')


def worksesh(request):
    if 'id' in request.session:
        this_user = filtro_usuario(request.session['id'])
    return render(request, 'worksesh.html', {'user':this_user})