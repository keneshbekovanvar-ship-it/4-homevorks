from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm
from django.conf import settings


def book_list(request):
    query = request.GET.get('q')
    books = Book.objects.all().order_by('-created_at')
    if query:
        books = books.filter(title__icontains=query)


    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book/book_list.html', {'page_obj': page_obj, 'query': query})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

# Создать новую книгу
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            # Скрытые поля через .env (например цена)
            if hasattr(settings, 'HIDE_PRICE') and settings.HIDE_PRICE:
                book = form.save(commit=False)
                book.price = 0
                book.save()
            else:
                form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book/book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book/book_confirm_delete.html', {'book': book})
