from django import forms
from .models import Book, Genre

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title','no_of_pages','isbn','image','description','genre','publishers','published_date')

class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = ('name',)
        