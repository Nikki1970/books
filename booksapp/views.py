from django.shortcuts import render, redirect
from booksapp.models import Book, Genre, Publisher
from django.views import generic
from .forms import BookForm, GenreForm
from .filters import BookFilter
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.


class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET,queryset=self.get_queryset())
        return context


class BookDetailView(generic.DetailView):
    model = Book


def book_new(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        form.author = request.user
        form.save()
        return redirect('list-of-books')
    context = {
        'form': form
    }
    return render(request, 'booksapp/book_edit.html',context)


def deleteBook(request, pk):
    book = Book.objects.get(id=pk)
    if request.method =="POST":
        book.delete()
        return redirect('list-of-books')
    context = {'book':book}
    return render(request, "booksapp/book_delete.html",context)


def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    form = BookForm(request.POST or None, instance = book)
    if form.is_valid():
        form.save()
        return redirect('list-of-books')
    context = {
        'form': form,
    }    
    return render(request, "booksapp/book_edit.html", context)


class GenreListView(generic.ListView):
    model = Genre

def create_genre(request):
    form = GenreForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list-of-genres')
    context = {
        'form': form
    }
    return render(request, 'booksapp/genre_edit.html',context)


def update_genre(request,pk):
    genre = Genre.objects.get(id = pk)
    form = GenreForm(request.POST or None, instance = genre)
    if form.is_valid():
        form.save()
        return redirect('list-of-genres')
    context = {
        'form': form,
    }    
    return render(request, "booksapp/genre_edit.html", context)


class Genredeleteview(generic.DeleteView):
    model = Genre
    success_url = reverse_lazy('list-of-genres')


class PublisherListView(generic.ListView):
    model = Publisher


class PublisherCreateView(generic.CreateView):
    model = Publisher
    fields = ['name']
    success_url = reverse_lazy('list-of-publishers')


class Publisherupdateview(generic.UpdateView):
    model = Publisher
    fields = ['name']
    success_url = reverse_lazy('list-of-publishers')


class Publisherdeleteview(generic.DeleteView):
    model = Publisher
    success_url = reverse_lazy('list-of-publishers')
