from django.urls import path
from .views import CategoryListView, CategoryDetailView, ProductListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_products'),
    path('products/', ProductListView.as_view(), name='product_list'),
]

