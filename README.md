# Django 3 Refresher - With Django Rest Framework

## Inspecting the current Django version, for future development
(from a tutorial & with thanks with thanks to [Krystian Czekalski](https://www.udemy.com/user/krystian-czekalski/))

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
    list_display = ['title', 'number', 'price']
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


## Django Rest framework

The [Django Rest framework](https://www.django-rest-framework.org/) contains reading material and guides for installation and use.

Tools used from the framework are:

1. Web browsable API
2. Authentication
3. Serialization
   

Installed apps: 

```python

INSTALLED_APPS = [
    # installed apps
    'rest_framework',
    'rest_framework.authtoken',
    'demo',
]

```

Adding the auth parameters for the rest framework:
(see official [Django docs](https://www.django-rest-framework.org/api-guide/authentication/))

```python

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}

```

Once the above changes have been made to the settings file, one will notice that trying to access the API will now be restricted. This is because Django now requires a user specific authentication token.  

NB See [Setting the permission policy](https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy)

![Restricted access to API](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/auth-1.png "RAuth token required for access to API")

To pass the auth token the url pattern Django has to obtain the token from the rest framework.  The token is generated from the authenticated user.  In this case you, the admin.  However a token hasn't been generated for you yet.  

```python

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('demo/', include('demo.urls')),
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token)
]

```

![Token](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/auth-2.png "To gain access to adding a token")

To generated at token for the admin user, use the token menu to create a new token then add the admin, yourself to the token.

![Token added](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/auth-3.png "A token is added to your name")

Once you have a token copy it for use with the Headers key value fields in Postman.  See the screenshots below.

![Un-Authenticated](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/auth-4.png "token shown, but not enabled by Postman")

![Authenticated](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/auth-5.png "token enabled by Postman showing MiniBookSerializer view")

![Authenticated view of specific book](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/auth-6.png "specific book from BookSerializerview")



### Web browsable API

The API is the URL connection consumed by Postman, sourced from Django.  i.e. the URL `http://127.0.0.1:8000/demo/` for the application results in a Django Rest API

![Django Rest API](https://github.com/ddeveloper72/django3-refresher/blob/master/static/img/drapi-1.png "Rest API landing page")

Selecting the API returns the contents of the API.  This is serialization.  We use Postman to interact with the API so we can perform CRUD operations to the data, using Get to get the data from the API and PUT to append data to the Model database (local sqlite3 provided by Django, but could be remote SQL or [MongoDB](https://djongo.readthedocs.io/docs/integrating-django-with-mongodb/))

```json

HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "title": "The Hobbit",
        "description": "'The Hobbit' is a tale of high adventure, undertaken by a company of dwarves in search of dragon-guarded gold. A reluctant partner in this perilous quest is Bilbo Baggins, a comfort-loving, unambitious hobbit.",
        "price": "5.00",
        "published": "2020-05-20",
        "is_published": false,
        "number": {
            "id": 2,
            "isbn_10": "9780007458",
            "isbn_13": "978-000745842"
        },
        "characters": [
            {
                "id": 2,
                "name": "Bilbo Baggins"
            }
        ],
        "authors": [
            {
                "id": 2,
                "name": "J. R. R",
                "surname": "Tolkien"
            }
        ]
    },
    {
        "id": 2,
        "title": "The Lord of the Rings",
        "description": "All three parts of the epic masterpiece The Lord of the Rings – The Fellowship of the Ring, The Two Towers & The Return of the King – available as one download, featuring the definitive edition of the text, hyperlinked footnotes and page references, and 3",
        "price": "9.99",
        "published": "2019-10-01",
        "is_published": true,
        "number": {
            "id": 3,
            "isbn_10": "0007322593",
            "isbn_13": "978-000732259"
        },
        "characters": [
            {
                "id": 1,
                "name": "Frodo Baggins"
            },
            {
                "id": 3,
                "name": "Gandalf"
            }
        ],
        "authors": [
            {
                "id": 2,
                "name": "J. R. R",
                "surname": "Tolkien"
            }
        ]
    },
    {
        "id": 3,
        "title": "Twilight: The Twilight Saga",
        "description": "About three things I was certain.\r\nFirst, Edward was a vampire.\r\n\r\nSecond, there was a part of him, and I didn't know how dominant that part might be, that thirsted for my blood.\r\n\r\nAnd Third, I was unconditionally and irrevocably in love with him.",
        "price": "4.45",
        "published": null,
        "is_published": false,
        "number": {
            "id": 4,
            "isbn_10": "0316015849",
            "isbn_13": "978-031601584"
        },
        "characters": [],
        "authors": [
            {
                "id": 1,
                "name": "Stephenie",
                "surname": "Meyer"
            }
        ]
    }
]

```

### Authentication



### Serialization

The serialization part of our Django serializer is the engine that drives what the contents of the API is going to be.  No serializer, no data.  An empty API.
Like a Model, we define what is displayed on the Django admin page.  The Serializer defines what objects from the model are serialized.

Multiple serializer can be used for different tasks and are NB Very important for refactoring your code.


Starting with the end- first. Think about refactoring.
say we have a library full of books.  Lots of books.  Would one want the API from Django to give you All of the book details all at once; the JSON file above for say 10,000+ books?  On Very Big data file? No.

A serializer provided that file.  However a second serializer can just as easily provide just the book ID and its title.  Less data, but it's a method of funnelling the data that is better managed by the front end.

```python

class MiniBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # specify the fields available from serializer
        fields = ['id', 'title']

```

The main serializer BookSerializer has four pre-serializers that provide additional objects from the different database models, namely book numbers with the ISBN, character and author objects.

The book numbers have a 1:1 relationship with the book db.  Characters may appear in different books by the dame author, so from a 1:many relationships with the book db.  Authors may write several books, so will have a many : many relationship with the book db.

```python

class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)
    
    class Meta:
        model = Book
        # specify the fields available from serializer
        fields = ['id', 'title', 'description',
                  'price', 'published', 'is_published',
                  'number', 'characters', 'authors']


```