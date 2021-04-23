from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title','no_of_pages','isbn','image','description','genre','publishers','published_date')
