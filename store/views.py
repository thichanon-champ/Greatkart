from django.shortcuts import render, get_object_or_404

from .models import Product
from category.models import Category
# Create your views here.


def store(request, category_slug=None):
    categories = None
    products = None
    
    
    if category_slug != None:
        categories = get_object_or_404(slug=category_slug)
        product = Product.objects.filter(category = categories, is_available =True)
        product_count = products.count()
    else:
        products= Product.objects.all().filter(is_available=True)
        product_count=products.count()
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {"products": products, "product_count": product_count}
    return render(request, "store/store.html", context)
