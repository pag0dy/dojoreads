from django.shortcuts import render, redirect, HttpResponse
from .forms import LogInForm, RegisterForm

def inicio(request):
    if request.method == 'GET':
        reg_form = RegisterForm()
        log_form = LogInForm()
        context = {
            'reg_form' : reg_form,
            'log_form' : log_form
        }
        return render(request, 'inicio.html', context)    

    return HttpResponse('Vista de inicio')

def registrar(request):
    if request.method == 'POST':
        if reg_form.is_valid():
            reg_form.save(commit=False)
            
    return HttpResponse('Registrar')

def ingresar(request):
    return HttpResponse('Ingresar')