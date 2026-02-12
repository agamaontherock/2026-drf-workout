from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict 
from django.http import QueryDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets

from .models import BookGenre, Book
from .serializers import BookModelSerializer, GenreModelSerializer
# Create your views here.
@api_view(["GET", "POST"])
def books(req):
    if req.method == "POST":
        request_body = req.POST
        print(req.POST)
        # Book.objects.create(title = request_body.get("title"),
        #                     author = request_body.get("author"),
        #                     inventory = int(request_body.get("inventory")))
        return Response()
    else:
        books = Book.objects.all()
        l = [model_to_dict(book) for book in books]
        return Response(data=l, status=status.HTTP_200_OK)


# @api_view(["GET"])
# def book_info(req, pk):
#     book = get_object_or_404(Book, pk=pk)
#     return Response(data=model_to_dict(book), status=status.HTTP_200_OK)

@api_view(["GET"])
def book_info(req, pk):
    book = get_object_or_404(Book, pk=pk)
    serializer = BookModelSerializer(book)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def genre_info(req, pk):
    book_genre = get_object_or_404(BookGenre, pk=pk)
    serializer = GenreModelSerializer(book_genre)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

class BookModelVset(viewsets.ModelViewSet):
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()