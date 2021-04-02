# Generated by Django 2.2.4 on 2021-04-02 15:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='alias',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(limit_value=3, message='El alias debe tener más de tres caracteres')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='Por favor ingrese un correo válido')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='El apellido debe tener más de dos caracteres')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=2, message='El nombre debe tener más de dos caracteres')]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=80, validators=[django.core.validators.MinLengthValidator(limit_value=8, message='La contraseña debe tener más de ocho caracteres')]),
        ),
    ]
