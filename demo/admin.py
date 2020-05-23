from django.contrib import admin
from .models import Book

# Register your models here.

# make specific fields available to book object in admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'description']
