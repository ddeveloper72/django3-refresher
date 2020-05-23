from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.


def first(request):
    books = Book.objects.all()

    return render(request, 'first_temp.html', {'books': books})
# crate a builtin view using viewsets
class BookViewSet(viewsets.MoedelViewSet):
