from django.contrib import admin
from .models import BookTitle, Book
# Register your models here.


class BookTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'author', 'created', 'updated')
    list_filter = ('publisher', 'author')
    search_fields = ('title', 'publisher__name', 'author__name')
    ordering = ('title',)
    date_hierarchy = 'created'


admin.site.register(BookTitle, BookTitleAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'book_id', 'created', 'updated')
    list_filter = ('title',)
    search_fields = ('title__title', 'book_id')
    ordering = ('title',)
    date_hierarchy = 'created'


admin.site.register(Book, BookAdmin)