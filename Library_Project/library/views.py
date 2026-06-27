from django.shortcuts import render, redirect
from .models import Book

# Home page
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})


# Add book
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        isbn = request.POST.get('isbn')
        quantity = request.POST.get('quantity')

        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            quantity=quantity
        )

        return redirect('home')

    return render(request, 'add_book.html')