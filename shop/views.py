from datetime import date
from django.shortcuts import render
from .models import Product


def shop_page(request):
    #products = Product.objects.filter(publishing_end_date > datetime.now())
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/shop.html', context)

def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(category=product_details.category)
    context = {
        'product': product_details,
        'related_products': related_products
    }
    return render(request, 'shop/product-details.html', context)

def wishlist(request):
    return render(request, 'shop/wishlist.html')
