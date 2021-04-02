from django.urls import path
from . import views

urlpatterns = [
    path('/<int:id>', views.book, name='book'),
    path('/agregar_libro', views.agregar_libro, name='agregar_libro'),
]