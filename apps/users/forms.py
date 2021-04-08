from django import forms
from .models import User, Company

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['permission_level', 'company']



class LoginForm(form.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']