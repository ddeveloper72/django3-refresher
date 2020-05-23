from django.contrib import admin
from .models import Book

# Register your models here.

# make specific fields available to book object in admin
# using fields or list_display
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'title', 'price']
