from django import forms
from .models import User

class RegisterForm(forms.ModelForm):

    confirmpass =  forms.CharField(max_length=80, label='Confirmar contraseña', widget= forms.PasswordInput())
    widgets = {
        'confirmpass' : forms.PasswordInput()
    }

    class Meta:
        model = User
        fields = ['name', 'last_name', 'alias', 'email', 'password', 'confirmpass']

        widgets = {
            'password': forms.PasswordInput()
        }

        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'password': 'Contraseña'
        }


class LogInForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }

        labels = {
            'password': 'Contraseña'
        }