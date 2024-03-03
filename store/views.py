from django.shortcuts import render
from .models import Product


def product_detail(request):
    return render(request, 'store/product_detail.html')

