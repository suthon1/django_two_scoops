from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

from .models import (
    Product,
    Category,
)

def categories(request):
    return {
        'categories': Category.objects.all()
    }


def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug, in_stock=True)
    return render(request,
    'store/products/detail.html',
    {'products': product})
