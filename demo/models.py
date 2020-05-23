from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(blank=False,
                             unique=True,
                             max_length=36)
    description = models.TextField(max_length=256,
                                   blank=True)

    price = models.DecimalField(default=0,
                                max_digits=3,
                                decimal_places=2)

    published = models.DateField(blank=True,
                                 null=True,
                                 default=None)
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/',
                              blank=True)
    
    
    # convert book object to user readable string in admin
    def __str__(self):
        return self.title

    class BookNumber(models.Model):
        isbn_10 = models.CharField(max_length=10)
        isbn_13 = models.CharField(max_length=13)
