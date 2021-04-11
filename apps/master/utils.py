from ..users.models import User, Company
from ..tasks.models import Project, Task, Assignments

def filtro_usuario(id_usuario):
    activo = User.objects.filter(id = id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontró el usuario'
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


def remove_blanks(string):
    return string.replace(' ', '')