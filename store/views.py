from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    popular_kits = Product.objects.filter(category='kit')[:4]  # Adjust category if needed
    return render(request, 'home.html', {
        'popular_kits': popular_kits
    })

def category_products(request, category_key):
    products = Product.objects.filter(category=category_key)
    return render(request, 'category_products.html', {
        'products': products,
        'category_key': category_key,
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Handle benefits as individual words (splitting on commas and then words)
    # Benefits split by comma (e.g. "Reusable, Compostable, Gentle")
    benefits_list = [b.strip() for b in product.benefits.split(',')] if product.benefits else []


    # Handle ingredients as trimmed comma-separated list
    ingredients_list = [i.strip() for i in product.ingredients.split(',')] if product.ingredients else []

    # Handle features as trimmed comma-separated list
    features_list = [f.strip() for f in product.features.split(',')] if product.features else []

    return render(request, 'product_detail.html', {
        'product': product,
        'benefits_list': benefits_list,
        'ingredients_list': ingredients_list,
        'features_list': features_list,
    })
