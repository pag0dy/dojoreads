from django.db import models
from ..user_app.models import User
from django.contrib import messages
from ..user_app.utils import existe, mayor_que, solo_letras


class BookManager(models.Manager):
    def validar_libro(self, postData):
        errors = {}
        mayor_que(postData['title'], 2, 'título')
        existe(postData['title'], 'título')

        return errors

class AuthorManager(models.Manager):
    def valida_autor(self, postData):
        errors = {}
        solo_letras(postData['nuevo_autor'], 'autor')
        mayor_que(postData['nuevo_autor'], 2, 'autor')
        existe(postData['nuevo_autor'], 'autor')

        return errors


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_lastname = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

    def __str__(self):
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

    def __str__(self):
        return self.title

