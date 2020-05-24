from django.contrib import admin
from .models import Book, BookNumber, Character, Author

# Register your models here.

# make specific fields available to book object in admin
# using fields or list_display
# adding a list_filter filter
# adding a search_fields filter
# adding more parametes to search_fields filter
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'number', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)
