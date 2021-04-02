from django.db import models
from ..book_app.models import Book
from ..user_app.models import User
from ..user_app.utils import existe, mayor_que

class ReviewManager(models.Manager):

    def validar_review(self, postData):
        errors = {}
        mayor_que(postData['review'], 5, 'review')
        existe(postData['review'], 'review')

        return errors

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

    def __str__(self):
        return self.book.title