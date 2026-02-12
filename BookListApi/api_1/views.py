from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Book
from django.forms.models import model_to_dict 
# Create your views here.
def books(req):
    books = Book.objects.all()
    l = [model_to_dict(book) for book in books]
    return JsonResponse({"books": l})

def book_info(req, pk):
    book = get_object_or_404(Book, pk=pk)
    obj = model_to_dict(book)
    return JsonResponse(obj)
