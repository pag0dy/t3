from django.db import models
from django.contrib import messages
from django.core.validators import MinLengthValidator, RegexValidator, validate_slug, EmailValidator
from .validators import letters_only, confirm_pass
import bcrypt

class UserManager(models.Manager):
    def validar_inicio(self, postData):
        errors = {}
        este_usuario = User.objects.filter(email = postData['email'])
        if len(este_usuario) == 0:
            errors['no_existe'] = 'El correo ingresado no está registrado'
        else:
            este_usuario = este_usuario[0]
            if bcrypt.checkpw(postData['password'].encode(), este_usuario.password.encode()):
                pass
            else:
                errors['clave_erronea'] = 'La clave ingresada no corresponde al usuario'

        return errors

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    n_workers = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

class User(models.Model):
    LEVELS = (
        ('a', 'admin'),
        ('b', 'project manager'),
        ('c', 'people manager'),
        ('d', 'staff')
    )

    ACCOUNT_TYPES = (
        ('SU', 'Solo User'),
        ('TA', 'Team Account')
    )

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    jobtitle = models.CharField(max_length=100)
    account_type = models.CharField(max_length=2, choices=ACCOUNT_TYPES, default='SU')
    email = models.EmailField()
    password = models.CharField(max_length=80)
    permission_level = models.CharField(max_length=1, choices=LEVELS)
    company = models.ForeignKey(Company, related_name='staff_members', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.email
