from django.urls import path
from . import views
urlpatterns=[
    path('', views.BookListView.as_view(), name="list-of-books"),
    path('detail/<int:pk>/', views.BookDetailView.as_view(), name="book-detail"),
    path('new/', views.book_new, name='new_book'),
    path('delete/<int:pk>/',views.deleteBook, name="delete_book"),
    path('update/<int:pk>/',views.updateBook, name="update_book"),
    path('genre/',views.GenreListView.as_view(),name="list-of-genres"),
    path('genrenew/',views.create_genre, name = "new_genre"),
    path('updategenre/<int:pk>/',views.update_genre, name="update_genre"),
    path('delete/genre/<int:pk>/', views.Genredeleteview.as_view(), name = 'delete_genre'),
    path('publishers/',views.PublisherListView.as_view(), name='list-of-publishers'),
    path('publishers/detail/<int:pk>/',views.PublisherDetailView.as_view(),name='publisher-detail'),
    path('newpublisher/',views.PublisherCreateView.as_view(), name='new_publisher'),
    path('updatepublisher/<int:pk>/', views.Publisherupdateview.as_view(),name='update_publisher'),
    path('delete/publisher/<int:pk>/', views.Publisherdeleteview.as_view(),name='delete_publisher'),
    path('genre/book/<int:pk>/', views.genre_books, name="genre-books"),
]