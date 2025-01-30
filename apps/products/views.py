from django.shortcuts import render, get_object_or_404
from apps.products.models import Product, Category, Images, Slider

# Create your views here.

def home(request):
    products = Product.objects.all()
    sliders = Product.objects.all()[:2]
    categories = Category.objects.all()[:6]
    banner = Slider.objects.all()  
    context = {
        'products':products,
        'sliders':sliders,
        'categories': categories,
        'banner': banner,
    }
    return render(request, 'index.html', context)

def product_detail(request, slug):
    categories = Category.objects.all()[:6]
    product = Product.objects.get(slug=slug)
    images = Images.objects.filter(product=product)
    context = {
        'categories':categories,
        'product':product,
    }
    return render(request, 'product-detail.html', context)


def category_detail(request, slug):
    categories = Category.objects.all()[:6]
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, status='True')
    context = {
        'categories':categories,
        'products':products,
        'category':category,
    }
    return render(request, 'category-detail.html', context)

def content(request):
    categories = Category.objects.all()[:6]
    return render(request, 'contact.html', {'categories': categories})

def contact(request):
    categories = Category.objects.all()[:6]
    return render(request, 'contact.html', {'categories':categories})
