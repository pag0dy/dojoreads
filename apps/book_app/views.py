from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author
from ..user_app.models import User
from ..review_app.models import Review

def filtro_usuario(id_usuario):
    activo = User.objects.filter(id = id_usuario)
    if activo:
        usuario_activo = activo[0]
        return usuario_activo
    else:
        mensaje = 'No se encontró el usuario'
        print(mensaje)
        return mensaje

def filtro_libro(id_libro):
    este_libro = Book.objects.filter(id = id_libro)
    if este_libro:
        este_libro = este_libro[0]
        return este_libro
    else:
        mensaje = 'No se encontró el libro'
        print('mensaje')
        return(mensaje)

def filtro_autor(id_autor):
    este_autor = Author.objects.filter(id=id_autor)
    if este_autor:
        este_autor = este_autor[0]
        return este_autor
    else:
        mensaje = 'No se encontró el autor'
        print('mensaje')
        return(mensaje)

def book(request, id):
    if 'id' in request.session:
        este_usuario = filtro_usuario(request.session['id'])
        este_libro = filtro_libro(id)
        
        context = {
            'book': este_libro,
            'este_usuario': este_usuario
        }

        return render(request, 'book.html', context)

def agregar_libro(request):
    if request.method == 'GET':    
        authors = Author.objects.all()
        print(authors)
        return render(request, 'add.html', {'authors':authors})
    
    else:
        errors = Book.objects.validar_libro(request.POST)
        errors = Author.objects.valida_autor(request.POST)
        errors = Review.objects.validar_review(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            
            return redirect('agregar_libro')

        else:
            este_usuario = filtro_usuario(request.session['id'])
            if este_usuario:
                if len(request.POST['nuevo_autor'])>1:
                    autor = request.POST['nuevo_autor']
                    nombre_autor = autor.split()[0]
                    apellido_autor = autor.split()[1]
                    autor_libro = Author.objects.create(author_name=nombre_autor, author_lastname=apellido_autor)
                else:
                    autor_libro = filtro_autor(request.POST['autor_lista'])
                
                nuevo_libro = Book.objects.create(title=request.POST['title'], author=autor_libro)
                nueva_review = Review.objects.create(content=request.POST['review'], rating=request.POST['rating'], book=nuevo_libro, user=este_usuario)
                id_libro = nuevo_libro.id

                return redirect('/books/' + str(id_libro))


