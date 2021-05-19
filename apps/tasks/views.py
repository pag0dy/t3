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

        return render(request, 'tasks/createProject.html', context)
    else:
        project_form = ProjectForm(request.POST)
        print(project_form.is_valid())
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

            return render(request, 'tasks/createProject.html', context)

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
            return render(request, 'tasks/project.html', context)

    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            nueva_tarea = form.save(commit=False)
            nueva_tarea.project = project
            nueva_tarea.save()
            mensaje = "Tarea agregada exitosamente!"
            messages.success(request, mensaje)
            assignment = Assignments.objects.create(staff_member=user, tasks=nueva_tarea, status='BL')
            assignment.save()
            return redirect('../project/' + str(project.id))


def addTask(request, methods=['POST']):
    staff = filtro_usuario(request.POST['staff_member'])
    task = filtro_tarea(request.POST['tasks'])
    asignar = Assignments.objects.create(staff_member=staff, tasks =task)
    asignar.save()
    mensaje = "Tarea agregada exitosamente!"
    messages.success(request, mensaje)
    return redirect('manage_team')

    
def editProject(request, id):
    user = filtro_usuario(request.session['id'])
    empresa = filtro_empresa(request.session['company'])
    project = filtro_proyecto(id)
    if request.method == 'GET':
        data = {
            'project_name': project.project_name,
            'client': project.client,
            'startDate': project.startDate,
            'endDate': project.endDate,
            'hours_assigned': project.hours_assigned,
            'project_lead': project.project_lead
        }
        form = ProjectForm(initial=data)
        context = {
            'form': form,
            'user': user,
            'company': empresa,
            'project':project
        }
        return render(request, 'tasks/editProject.html', context)

    else:
        form = ProjectForm(request.POST)
        if form.is_valid():
            project.project_name = request.POST['project_name']
            project.client = request.POST['client']
            project.startDate = request.POST['startDate']
            project.endDate = request.POST['endDate']
            project.hours_assigned = request.POST['hours_assigned']
            project.project_lead = filtro_usuario(request.POST['project_lead'])
            project.save()
            message = "Proyecto actualizado exitosamente"
            messages.success(request, message)
            return redirect('../edit/' + str(project.id))
        else:
            context = {
                'form': form,
                'user': user,
                'company':company
            }
            return render(request, 'editProject.html', context)

def removeProject(request, id):
    user = filtro_usuario(request.session['id'])
    empresa = filtro_empresa(request.session['company'])
    project = filtro_proyecto(id)
    project.delete()
    message = "Proyecto eliminado"
    messages.success(request, message)
    return redirect('createProject')