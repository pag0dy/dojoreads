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


class User(models.Model):
    name = models.CharField(max_length=100, validators = [MinLengthValidator(limit_value = 2, message = 'El nombre debe tener más de dos caracteres')])
    last_name = models.CharField(max_length=100, validators =[MinLengthValidator(limit_value = 2, message ='El apellido debe tener más de dos caracteres')])
    alias = models.CharField(max_length=50, validators =[MinLengthValidator(limit_value = 3, message ='El alias debe tener más de tres caracteres')])
    email = models.EmailField(validators=[EmailValidator(message = 'Por favor ingrese un correo válido')])
    password = models.CharField(max_length=80, validators =[MinLengthValidator(limit_value = 8, message ='La contraseña debe tener más de ocho caracteres')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return self.alias