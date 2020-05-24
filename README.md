# Django 3 Refresher

## Inspecting the current Django version, for future development

In this Django Demonstration, the goal was to setup models that demonstrate the use of 1:1, 1:many and many:many relationships.  Then while working with the models, Django rest Framework is user to serialize the data from the models by means of view functions.  Postman was then used to visualize the data in JSON format.

The demonstration also uses secure tokens to facilitate user authentication between the font-end Postman and backend Django.

### Leaning Outcomes

- Using Django 3 as opposed to 2 used in pervious projects
- Customizing the data used in admin to provide better user experiences as opposed to working data from the backend to be represented on a Django's front-end framework.
- Using Django Rest Framework for the first time
- Using Postman to send and receive data from a frontend environment to Django
- Using authentication tokens to enable Django and postman to pass data securely

### Code snippets

``` python

from django.contrib import admin
from .models import Book, BookNumber, Character, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'title', 'price']
    list_filter = ['published']
    search_fields = ['title', 'description']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)

```

The Django app being used is managed from the admin interface.  To do so, all the relevant data fields were made available by registering them directly in the admin.

![Admin](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/admin-1.png "Demo from admin")

Selecting books, demonstrates the separated tables registered in the admin above.

![Admin](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/admin-2.png "Books from admin")

### Showing object in admin as a string

```python

class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book,
                             on_delete=models.CASCADE,
                             related_name='characters')
    # convert object to string
    def __str__(self):
        return self.name

```

The character name uses a 1:many relationship to the Book table.  i.e the same character may appear in several books- one to many.  Here the characters are also converted from an object to a string so we see the actual character name.

![Characters as string](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/admin-3.png "Character objects converted to string")

![Characters as objects](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/admin-4.png "Character objects prior conversion to string")