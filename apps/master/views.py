from django.shortcuts import render, redirect, HttpResponse
from ..users.forms import RegistrationForm, LoginForm, CompanyForm, AddStaffForm
from ..users.models import User, Company
from ..tasks.models import Assignments, Project, Task
from django.contrib import messages
from .utils import filtro_usuario, filtro_usuario_email, filtro_empresa, remove_blanks
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
            if este_usuario.company != 'No company':
                esta_empresa = este_usuario.company               
                request.session['company'] = esta_empresa.id
            return redirect('home')

    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            nuevo_usuario = reg_form.save(commit=False)
            password = reg_form.clean_password()
            
            if password:
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
                nuevo_usuario.password = pw_hash
                if nuevo_usuario.account_type == 'SU':
                    nuevo_usuario.company = NoCompany
                    nuevo_usuario.permission_level = 'a'
                    nuevo_usuario.save()
                    crearSesion(request, nuevo_usuario)
                    return redirect('home')
                else:
                    comp_form = CompanyForm(request.POST)
                    if comp_form.is_valid():
                        nueva_empresa = comp_form.save()
                        request.session['company'] = nueva_empresa.id
                        nuevo_usuario.company = nueva_empresa
                        nuevo_usuario.permission_level = 'a'
                        nuevo_usuario.save()
                        crearSesion(request, nuevo_usuario)
                        return redirect('team_setup')

        else:                    
            return redirect('register')

    else:
        reg_form = RegistrationForm()
        company_form = CompanyForm()
        context = {
            'reg_form' : reg_form,
            'company_form': company_form
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

def team_setup(request):
    if request.method == 'GET':
        form = AddStaffForm()
        company = filtro_empresa(request.session['company'])
        context = {
            'form':form, 
            'company':company
        }
        return render(request, 'team_setup.html', context)

    else:
        form = AddStaffForm(request.POST)
        if form.is_valid():
            nuevo_staff = form.save(commit=False)
            empresa = filtro_empresa(request.session['company'])
            nombre_empresa = remove_blanks(empresa.company_name)
            print(nombre_empresa)
            if len(nombre_empresa) < 4:
                password = nuevo_staff.name + nombre_empresa
            else:
                nombre_empresa = nombre_empresa[0:4]
                print(nombre_empresa)
                staffName = nuevo_staff.name
                password = staffName + nombre_empresa
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
                nuevo_staff.password = pw_hash
                nuevo_staff.account_type = 'TA'
                nuevo_staff.company = empresa
                nuevo_staff.save()
                mensaje = "Colaborador agregado exitosamente!"
                messages.success(request, mensaje )
                return redirect('team_setup')


        else:
            context = {
                'form': AddStaffForm()
            }
            return render(request, 'team_setup.html', {'form':form})

def manage_team(request):
    if request.method == 'GET':
        company = filtro_empresa(request.session['company'])
        user = filtro_usuario(request.session['id'])
        assignments = Assignments.objects.all()
        context = {
            'company':company,
            'user':user,
            'assignments':assignments
        }
        return render(request, 'manage_team.html', context)


def worksesh(request):
    if 'id' in request.session:
        this_user = filtro_usuario(request.session['id'])
    return render(request, 'worksesh.html', {'user':this_user})