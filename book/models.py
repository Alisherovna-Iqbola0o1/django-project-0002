
from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    total_books = models.PositiveIntegerField()
    nationality = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    class CoverType(models.TextChoices):
        HARD = 'Hard', 'Hard cover'
        SOFT = 'Soft', 'Soft cover'

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pages = models.PositiveIntegerField()
    price = models.FloatField()
    cover = models.CharField(max_length=10, choices=CoverType.choices)
    image = models.ImageField(upload_to='books/')
    total_sold = models.PositiveIntegerField(default=0)
    in_stock = models.PositiveIntegerField(default=0)
#   created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    books = models.ManyToManyField(Book)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    total_sold_books = models.PositiveIntegerField(default=0)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)





