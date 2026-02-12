from . import views

from django.urls import path

urlpatterns = [
    path('books/', views.books),
    path('books/<int:pk>', views.book_info),
]