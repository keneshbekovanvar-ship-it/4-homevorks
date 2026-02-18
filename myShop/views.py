from django.views.generic import ListView, DetailView
from .models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'myShop/categories.html'
    context_object_name = 'categories'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'myShop/category_products.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()
        return context



class ProductListView(ListView):
    model = Product
    template_name = 'myShop/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.select_related('category')

# Create your views here.
