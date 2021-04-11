from django import forms
from .models import Project, Task, Assignments
from django.core.exceptions import ValidationError

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['company']

        widgets = {
            'startDate': forms.DateInput(
                attrs = {
                    'type': 'date'
                }
            ),
            'endDate': forms.DateInput(
                attrs = {
                    'type': 'date'
                }
            )
        }

        labels = {
            'project_name': 'Nombre del Proyecto',
            'client': 'Cliente',
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Término',
            'hours_assigned': 'Horas asigndas',
            'project_lead': 'Responsable'
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['project', 'assigned_to']

        widgets = {
            'startDate': forms.DateInput(
                attrs = {
                    'type': 'date'
                }
            ),
            'endDate': forms.DateInput(
                attrs = {
                    'type': 'date'
                }
            )
        }

        labels = {
            'task_name': 'Nombre de la tarea',
            'startDate': 'Fecha de Inicio',
            'endDate': 'Fecha de Término',
            'hours_assigned': 'Horas asigndas',
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignments
        exclude = ['status']

        labels = {
            'staff_member': 'Asignar a',
            'task': 'Tarea',
        }