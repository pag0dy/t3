from ..users.models import User, Company
from ..tasks.models import Project, Task, Assignments
from .models import WorkSession

def filtro_worksesh(id):
    worksesh = WorkSession.objects.filter(id=id)
    if worksesh:
        worksesh = worksesh[0]
        return worksesh

def filtro_usuario(id_usuario):
    activo = User.objects.filter(id = id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontrĂ³ el usuario'
        print(mensaje)
        return mensaje

def filtro_usuario_email(email):
    activo = User.objects.filter(email = email)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo

def filtro_empresa(id):
    company = Company.objects.filter(id=id)
    if company:
        this_company = company[0]
        return this_company

def filtro_proyecto(id):
    project = Project.objects.filter(id=id)
    if project:
        this_project = project[0]
        return this_project

def filtro_tarea(id):
    task = Task.objects.filter(id=id)
    if task:
        this_task = task[0]
        return this_task


def remove_blanks(string):
    return string.replace(' ', '')