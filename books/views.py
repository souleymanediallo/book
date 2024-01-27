from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, BookTitle
from .forms import BookForm
# Create your views here.


def home(request):
    book_titles = BookTitle.objects.all()
    books = Book.objects.all()
    context = {'books': books, 'book_titles': book_titles}
    return render(request, 'books/index.html', context)


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/book-list.html', context)


def book_detail(request, pk):
    book_title = get_object_or_404(BookTitle, id=pk)
    context = {'book_title': book_title}
    return render(request, 'books/book-detail.html', context)


def book_new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book-new.html', {})


def book_edit(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'books/book-edit.html', context)


def book_delete(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    context = {'book': book}
    return render(request, 'books/book-delete.html', context)