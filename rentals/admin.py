from django.contrib import admin
from .models import Rental
# Register your models here.


class RentalAdmin(admin.ModelAdmin):
    list_display = ('customer', 'book', 'rent_start_date', 'rent_end_date', 'created', 'updated')


admin.site.register(Rental, RentalAdmin)
