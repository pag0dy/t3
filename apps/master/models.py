from django.db import models
from ..tasks.models import Assignments, Task, Project

class WorkSession(models.Model):
    startTime = models.DateTimeField(auto_now_add=True)
    stopTime = models.DateTimeField(auto_now=True)
    assignment = models.ForeignKey(Assignments, related_name='worksessions', on_delete=models.CASCADE)
    comment = models.TextField(blank=True)


