from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField('ISBN', max_length = 20, unique = True)
    no_of_pages = models.IntegerField()
    image = models.ImageField(null=True,blank=True)
    description = models.TextField(max_length = 2000)
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    genre  = models.ManyToManyField('Genre')
    publishers = models.ManyToManyField('Publisher')
    published_date = models.DateField(null = True, blank = True)
    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name