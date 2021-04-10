from django import forms
from .models import User, Company
from .validators import letters_only, confirm_pass
from django.core.exceptions import ValidationError
import bcrypt

class RegistrationForm(forms.ModelForm):

    confirmpass = forms.CharField(max_length=80, label='Confirmar contraseña', widget= forms.PasswordInput())
    widgets = {
        'confirmpass' : forms.PasswordInput()
    }
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
        }),
        error_messages={'invalid': 'Por favor ingrese un email válido'}
    )
    
    class Meta:
        model = User
        exclude = ['permission_level', 'company']

        widgets = {
            'password' : forms.PasswordInput()
        }

        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'jobtitle': 'Cargo',
            'account_type': 'Tipo de cuenta',
            'password': 'Contraseña'
        }


    def clean_password(self):
        data = self.cleaned_data['password']
        confirm =  self.data['confirmpass']
        errors = []
        errors.append(confirm_pass(data, confirm))
        if errors == [None]:
            return data
        else:
            raise ValidationError(errors)

    def clean_user(self):
        data = self.cleaned_data['email']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }

        labels = {
            'password': 'Contraseña'
        }


class AddStaffForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'lastname', 'email', 'jobtitle', 'permission_level']

        email = forms.EmailField(
            widget=forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            error_messages={'invalid': 'Por favor ingrese un email válido'}
        )

        labels = {
            'name': 'Nombre',
            'lastname': 'Apellido',
            'jobtitle': 'Cargo',
            'permission_level': 'Tipo de usuario',
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

        labels = {
            'company_name': 'Nombre de la empresa',
            'n_workers': 'Número de trabajadores'
        }