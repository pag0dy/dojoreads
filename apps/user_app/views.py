from django.shortcuts import render, redirect, HttpResponse

def inicio(request):
    return HttpResponse('Vista de inicio')