from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.contrib.auth.decorators import login_required


def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/book_list.html', {'books': books})

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.is_available:
        book.is_available = False
        book.borrowed_by = request.user
        book.save()
    return redirect('book_list')
