from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Cart
from products.models import Product
# Create your views here.


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart = Cart.objects.get(user=request.user)

    cart.items.add(product)

    return redirect('cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    cart = Cart.objects.get(user=request.user)

    cart.items.remove(product)

    return redirect('cart')


@login_required
def remove_all_from_cart(request):
    cart = request.user.cart
    cart.items.clear()

    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    products = user.cart.items.all()
    return render(request, 'carts/cart.html', {'products': products})
