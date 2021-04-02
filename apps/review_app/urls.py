from django.urls import path
from . import views

urlpatterns = [
    path('agregar_review', views.agregar_review, name='agregar_review'),
    path('home', views.home, name='home'),
    path('eliminar_review', views.eliminar_review, name='eliminar_review')
]