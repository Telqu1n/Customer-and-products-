from django.shortcuts import render
from .models import Customer, Product

# Create your views here.


def home(request):
    products = Product.objects.all()
    return render(request, 'customer/index.html',{
        'products': products
    })