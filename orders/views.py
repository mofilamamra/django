from django.shortcuts import render, redirect
from .models import Order
# Create your views here.


def order_list(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.all()
        return render(request, 'orders/order-list.html', {'orders': orders})
    else:
        return redirect('products_list')
