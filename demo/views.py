from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book

# Create your views here.


class Another(View):

    book = Book.objects.get(id=1)
    # setup empty string as output
    output = f"We have {book.title}  with ID {book.id}<br>"
    # for book in books:

        # concatenate the strings together else last line overwrites 1st
        # output += f"We have {book.title}  with ID {book.id}<br>"

    def get(self, request):
        return HttpResponse(self.output)


def first(request):
    return HttpResponse('First message from views')
