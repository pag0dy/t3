from django.shortcuts import render, redirect, HttpResponse
from .models import Project, Task, Assignments
from ..users.models import User, Company
from django.contrib import messages
from ..master.utils import filtro_empresa, filtro_usuario, filtro_proyecto, filtro_tarea
from .forms import ProjectForm, TaskForm

def createProject(request):
    if request.method == 'GET':
        user = filtro_usuario(request.session['id'])
        empresa = filtro_empresa(request.session['company'])
        form = ProjectForm()
        context = {
            'form': form,
            'user': user,
            'company': empresa
        }

        return render(request, 'createProject.html', context)
    else:
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            nuevo_proyecto = project_form.save(commit=False)
            nuevo_proyecto.company = filtro_empresa(request.session['company'])
            nuevo_proyecto.save()
            mensaje = "Proyecto agregado exitosamente!"
            messages.success(request, mensaje)
            return redirect('createProject')

        else:
            user = filtro_usuario(request.session['id'])
            empresa = filtro_empresa(request.session['company'])
            context = {
                'form': project_form,
                'user': user,
                'company': empresa
            }

            return render(request, 'createProject.html', context)

def project(request, id):
    user = filtro_usuario(request.session['id'])
    empresa = filtro_empresa(request.session['company'])
    project = filtro_proyecto(id)
    if request.method == 'GET':
        form = TaskForm()
        if project:
            context = {
                'project': project,
                'form': form,
                'user':user,
                'company': empresa

            }
            return render(request, 'project.html', context)

    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            nueva_tarea = form.save(commit=False)
            nueva_tarea.project = project
            nueva_tarea.save()
            mensaje = "Tarea agregada exitosamente!"
            messages.success(request, mensaje)
            return redirect('../project/' + str(project.id))


def addTask(request, methods=['POST']):
    staff = filtro_usuario(request.POST['staff_member'])
    task = filtro_tarea(request.POST['tasks'])
    asignar = Assignments.objects.create(staff_member=staff, tasks =task)
    asignar.save()
    mensaje = "Tarea agregada exitosamente!"
    messages.success(request, mensaje)
    return redirect('manage_team')

    
