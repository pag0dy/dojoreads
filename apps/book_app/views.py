from django.shortcuts import render, redirect, HttpResponse

def books(request):
    return HttpResponse('Vista de books')