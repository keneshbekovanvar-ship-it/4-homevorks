from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.conf import settings
from .models import Book
from .forms import BookForm



class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'page_obj'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        books = Book.objects.all().order_by('-created_at')

        if query:
            books = books.filter(title__icontains=query)

        return books

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'book'



class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = reverse_lazy('book_list')

    def form_valid(self, form):
        if hasattr(settings, 'HIDE_PRICE') and settings.HIDE_PRICE:
            book = form.save(commit=False)
            book.price = 0
            book.save()
            self.object = book
            return super().form_valid(form)
        else:
            return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
