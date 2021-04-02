from django.shortcuts import render, redirect, HttpResponse
from .models import Book
from ..book_app.views import filtro_libro, filtro_usuario
from ..review_app.models import Review
from ..user_app.models import User
from ..user_app.views import filtro_usuario

def filtro_review(id_rev):
    este_rev = Review.objects.filter(id=id_rev)
    if este_rev:
        este_rev = este_rev[0]
        return este_rev
    else:
        mensaje = 'No se encontró el review'
        print('mensaje')
        return(mensaje)


def agregar_review(request, methods=['POST']):
        errors = Review.objects.validar_review(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('../books/' + str(request.POST['id_libro']))
        
        else:
            if 'id' in request.session:
                usuario = filtro_usuario(request.session['id'])
                libro = filtro_libro(request.POST['book_id'])

                nueva_review = Review.objects.create(content=request.POST['review'], rating=request.POST['rating'], book = libro, user = usuario)

                return redirect('../books/' + str(request.POST['book_id']))

            else:
                return HttpResponse('Debes iniciar sesión para postear un review')

def home(request):
    if 'id' in request.session:
        este_usuario = filtro_usuario(request.session['id'])
        libros = Book.objects.all()
        reviews = Review.objects.all().order_by('-created_at')[:3]
        context = {
            'este_usuario' : este_usuario,
            'books' : libros,
            'reviews' : reviews
        }
        return render(request, 'home.html', context)

def eliminar_review(request, methods=['POST']):
    if 'review_id' in request.POST:
        review_eliminar = filtro_review(request.POST['review_id'])
        review_eliminar.delete()
        return redirect('home')


