
from django.shortcuts import render
from django.utils import timezone
from .models import Product
# Create your views here.


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products-list.html', {'products': products})


def say_hi(request, name):
    return render(request, 'say-hi.html', {'name': name})

    # Show time.


def show_time(request):

    now = timezone.now()
    return render(request, 'show-time.html', {'now': now})
