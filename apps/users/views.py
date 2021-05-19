from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationFormTeam, RegistrationFormSolo, LoginForm, EditUserForm, EditPassForm, CompanyForm, StaffForm
from .models import User, Company
from ..tasks.models import Task, Assignments, Project
from django.contrib import messages
import bcrypt
from ..master.utils import filtro_usuario_email, filtro_usuario, filtro_empresa

def user(request):
    this_user = filtro_usuario(request.session['id'])
    data = {
            'name':this_user.name,
            'lastname':this_user.lastname,
            'email':this_user.email,
        }
    editform = EditUserForm(initial=data)
    editpass = EditPassForm()
    context = {
            'user':this_user,
            'editform':editform,
            'editpass': editpass
    }
    return render(request, 'users/mi_info.html', context)


def editarperfil(request, methods=['POST']):
    this_user = filtro_usuario(request.session['id'])
    editform = EditUserForm(request.POST)
    if editform.is_valid():
        this_user.name = request.POST['name']
        this_user.lastname = request.POST['lastname']
        this_user.email = request.POST['email']
        this_user.save()
        mensaje = 'Has actualizado tu perfil exitosamente!'
        messages.success(request, mensaje)
        return redirect('user')
    else:
        context = {
            'editform': editform,
            'editpass': EditPassForm()
        }
        return render(request, 'users/mi_info.html', context)

def editarpass(request, methods=['POST']):
    this_user = filtro_usuario(request.session['id'])
    editpass = EditPassForm(request.POST)
    if editpass.is_valid():
        password = editpass.clean_password() 
        if password:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
            this_user.password = pw_hash
            this_user.save()
            mensaje = 'Has actualizado tu contraseña exitosamente!'
            messages.success(request, mensaje)
            return redirect('home')
    else:
        context = {
            'editform': EditUserForm(),
            'editpass': editpass
        }
        return render(request, 'users/editarperfil.html', context)
        
def companyprofile(request):
    this_user = filtro_usuario(request.session['id'])
    company = filtro_empresa(request.session['company'])
    context = {
        'user':this_user,
        'company':company
    }
    return render(request, 'users/company.html', context)

def editcompany(request):
    this_user = filtro_usuario(request.session['id'])
    company = filtro_empresa(request.session['company'])
    if request.method == 'GET':
        data = {
            'company_name':company.company_name,
            'n_workers':company.n_workers,
        }
        form = CompanyForm(initial=data)
        context = {
            'form': form,
            'user': this_user,
            'company':company
        }
        return render(request, 'users/editcompany.html', context)
    else:
        form = CompanyForm(request.POST)
        if form.is_valid():
            company.company_name = request.POST['company_name']
            company.n_workers = request.POST['n_workers']
            company.save()
            mensaje = 'Has actualizado tu la información de tu empresa!'
            messages.success(request, mensaje)
            return redirect('home')

    return HttpResponse('hola')

def staff_info(request, id):
    this_user = filtro_usuario(request.session['id'])
    company = filtro_empresa(request.session['company'])
    staff = filtro_usuario(id)
    context = {
        'user':this_user,
        'company':company,
        'staff':staff
    }
    return render(request, 'users/staff_info.html', context)

def editstaff(request, id):
    this_user = filtro_usuario(request.session['id'])
    company = filtro_empresa(request.session['company'])
    staff = filtro_usuario(id)
    if request.method=='GET':

        data = {
            'name': staff.name,
            'lastname': staff.lastname,
            'jobtitle': staff.jobtitle,
            'email': staff.email,
            'permission_level': staff.permission_level
        }
        form = StaffForm(initial=data)
        context = {
            'form':form,
            'user':this_user,
            'company':company,
            'staff':staff
        }
        return render(request, 'users/editstaff.html', context)
    else:
        form = StaffForm(request.POST)
        if form.is_valid():
            staff.name = request.POST['name']
            staff.lastname = request.POST['lastname']
            staff.jobtitle = request.POST['jobtitle']
            staff.email = request.POST['email']
            staff.permission_level = request.POST['permission_level']
            staff.save()
            mensaje = "Colaborador editado exitosamente!"
            messages.success(request, mensaje)
            return redirect('companyprofile')
        else:
            context = {
                'form': form,
                'user':this_user,
                'company':company,
                'staff':staff
            }
            return render(request, 'editstaff.html', context)

def deletestaff(request, methods=['POST']):
    eliminar_staff = filtro_usuario(request.POST['staff_id'])
    eliminar_staff.delete()
    mensaje = "Colaborador eliminado"
    messages.success(request, mensaje)
    return redirect('companyprofile')