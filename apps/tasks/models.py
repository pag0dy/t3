from django.db import models
from ..users.models import User, Company

class Project(models.Model):
    project_name = models.CharField(max_length=254)
    client = models.CharField(max_length=100)
    startDate = models.DateField()
    endDate = models.DateField()
    hours_assigned = models.PositiveIntegerField()
    project_lead = models.ForeignKey(User, related_name='projects_assigned', on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, related_name='company_projects', on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Task(models.Model):
    task_name = models.CharField(max_length=254)
    startDate = models.DateField()
    endDate = models.DateField()
    hours_assigned = models.PositiveIntegerField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, through='Assignments', blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

class Assignments(models.Model):
    STATUS = (
    ('ST', 'Started'),
    ('CM', 'Completed'),
    ('IP', 'In Progress'),
    ('BL', 'Backlog'),
    ('OH', 'On Hold'),
    ('BD', 'Blocked'),
    ('DM', 'Dismissed')
    )

    staff_member = models.ForeignKey(User, on_delete=models.CASCADE)
    tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS, default='BL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


