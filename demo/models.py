from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(blank=False,
                             unique=True,
                             max_length=36)