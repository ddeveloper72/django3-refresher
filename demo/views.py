from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

# Create your views here.


def first(request):
    return render(request, 'first_temp.html')
