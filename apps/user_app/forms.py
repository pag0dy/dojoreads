from django import forms
from .models import User
from django.core.exceptions import ValidationError
from .validators import letters_only, confirm_pass
import bcrypt

def filtro_usuario_email(email):
    activo = User.objects.filter(email = email)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
 
  

class RegisterForm(forms.ModelForm):

    confirmpass = forms.CharField(max_length=80, label='Confirmar contraseña', widget= forms.PasswordInput())
    widgets = {
        'confirmpass' : forms.PasswordInput()
    }
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control w-75',
        }),
        error_messages={'invalid': 'Por favor ingrese un email válido'}
    )

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

 