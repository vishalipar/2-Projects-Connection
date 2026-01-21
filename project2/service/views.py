from django.shortcuts import render
from .services import ProductAPIClient

def product_list(request):
    """View to display products from Project 1"""
    products = ProductAPIClient.get_all_products()
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, pk):
    """View to display single product from Project 1"""
    product = ProductAPIClient.get_product(pk)
    return render(request, 'products/detail.html', {'product': product})