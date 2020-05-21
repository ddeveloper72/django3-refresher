from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.


class Another(View):

    books = Book.objects.all()

    output = f"We have {len(books)}  books in our DB"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')