from django.shortcuts import render
from booksapp.models import Book
from django.views import generic
from .forms import BookForm
from django.contrib.auth.models import User
# Create your views here.
class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book

def book_new(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form = form.save(commit=False)
        form.author = request.User
        form.save()
        return redirect('list-of-books')
    context = {
        'form': form
    }
    return render(request, 'booksapp/book_edit.html',context)
