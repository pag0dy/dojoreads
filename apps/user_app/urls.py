from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar', views.registrar, name='registrar'),
    path('ingresar', views.ingresar, name='ingresar'),
    path('user/<int:id>', views.user, name='user'),
    path('salir', views.salir, name='salir')
]