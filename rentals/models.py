from django.db import models
from books.models import Book
from customers.models import Customer
from datetime import timedelta


STATUS_CHOICES = (
        ('#01', 'rented'),
        ('#02', 'returned'),
        ('#03', 'lost'),
        ('#04', 'delayed'),
    )


# Create your models here.
class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_rentals')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_rentals')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='#01')
    rent_start_date = models.DateField()
    rent_end_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    is_closed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.book_id} rented by {self.customer}"

    def save(self, *args, **kwargs):
        if not self.rent_end_date:
            self.rent_end_date = self.rent_start_date + timedelta(days=14)