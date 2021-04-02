from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import LogInForm, RegisterForm, ValidationError
from .models import User
import bcrypt

def crearSesion(request, usuario):
    request.session['id'] = usuario.id
    print('Sesión creada')
    return True

def filtro_usuario(id_usuario):
    activo = User.objects.filter(id = id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontró el usuario'
        print(mensaje)
        return mensaje

def filtro_usuario_email(email):
    activo = User.objects.filter(email = email)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo

def inicio(request):
    if 'id' in request.session:
        del request.session['id']
    else:
        pass
    reg_form = RegisterForm()
    log_form = LogInForm()
    context = {
        'reg_form' : reg_form,
        'log_form' : log_form
    }
    return render(request, 'inicio.html', context)    

def registrar(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            nuevo_usuario = form.save(commit=False)
            password = form.clean_password()
            
            if password:
                pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() 
                nuevo_usuario.password = pw_hash
                nuevo_usuario.save()
                crearSesion(request, nuevo_usuario)
                return redirect('review/home')

            else:                    
                return redirec('inicio')

        else:
            context = {
                'reg_form' : form,
                'log_form' : LogInForm()
            }
            return render(request, 'inicio.html', context)

def ingresar(request):
    if request.method == 'POST':
        errors = User.objects.validar_inicio(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return redirect('inicio')
        
        else:
            este_usuario = filtro_usuario_email(request.POST['email'])
            crearSesion(request, este_usuario)
            return redirect('review/home')

    return HttpResponse('Error!')

def user(request, id):
    usuario = filtro_usuario(id)
    if usuario:
        context = {
            'usuario':usuario
        }
        return render(request, 'user.html', context)
    else:
        return HttpResponse('No se encontró el usuario')


def salir(request):
    try:
        del request.session['id']
        return redirect('inicio')
    except:
        return HttpResponse('no has iniciado una sesión')