from django.urls import path
from . import views
urlpatterns=[
    path('', views.BookListView.as_view(), name="list-of-books"),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
    path('new/', views.book_new, name='new_book'),
]