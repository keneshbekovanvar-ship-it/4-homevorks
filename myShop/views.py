from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'myShop/categories.html', {
        'categories': categories
    })


def product_list(request):
    products = Product.objects.select_related('category')
    return render(request, 'myShop/products.html', {
        'products': products
    })


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, 'myShop/category_products.html', {
        'category': category,
        'products': products
    })


# Create your views here.
