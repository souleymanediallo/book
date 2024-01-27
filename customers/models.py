from django.db import models
from django.utils.text import slugify

from books.models import Book


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, blank=True, unique=True)
    additional_info = models.TextField(blank=True)
    ratting = models.PositiveSmallIntegerField(default=50)
    books = models.ManyToManyField(Book, related_name='customers', blank=True)
    book_count = models.PositiveSmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        if not self.username:
            username = slugify(f"{self.first_name}.{self.last_name}")
            ex = __class__.objects.filter(username=username).exists()
            while ex:
                i = len(__class__.objects.filter(first_name=self.first_name, last_name=self.last_name))
                username = slugify(f"{self.first_name}.{self.last_name}.{i+1}")
                ex = __class__.objects.filter(username=username).exists()
            self.username = username
        return super().save(*args, **kwargs)