from django.shortcuts import render, redirect
from booksapp.models import Book
from django.views import generic
from .forms import BookForm
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
        form = form.save(commit=False)
        form.save()
        return redirect('list-of-books')
    context = {
        'form': form
    }
    return render(request, 'booksapp/book_edit.html',context)

def deleteBook(request, pk):
    instance = Book.objects.get(id=pk)
    if request.method =="POST":
        instance.delete()
        return redirect('list-of-books')
    context = {'form': instance,'book':instance}
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