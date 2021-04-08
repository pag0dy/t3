from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    n_workers = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(models.Model):
    LEVELS = (
        ('a', 'admin'),
        ('b', 'project manager'),
        ('c', 'people manager'),
        ('d', 'staff')
    )

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    permission_level = models.CharField(max_length=1, choices=LEVELS)
    company = models.ForeignKey(Company, related_name='staff_members', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)