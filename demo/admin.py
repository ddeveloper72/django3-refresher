from django.contrib import admin
from .models import Book, BookNumber

# Register your models here.

# make specific fields available to book object in admin
# using fields or list_display
# adding a list_filter filter
# adding a search_fields filter
# adding more parametes to search_fields filter
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'title', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']


admin.site.register(BookNumber)
