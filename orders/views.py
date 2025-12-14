from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

@login_required
def cart_view(request):
    cart, _ = Order.objects.get_or_create(user=request.user, status='Cart')
    return render(request, 'orders/cart.html', {'cart': cart})

@login_required
def update_item(request, item_id):
    cart = get_object_or_404(Order, user=request.user, status='Cart')
    order_item = get_object_or_404(OrderItem, id=item_id, order=cart)

    if request.method == 'POST':
        order_item.quantity = int(request.POST.get('quantity', 1))
        order_item.save()
    return redirect('cart_view')

@login_required
def delete_item(request, item_id):
    cart = get_object_or_404(Order, user=request.user, status='Cart')
    order_item = get_object_or_404(OrderItem, id=item_id, order=cart)
    order_item.delete()
    return redirect('cart_view')

@login_required
def place_order(request):
    cart = get_object_or_404(Order, user=request.user, status='Cart')

    # prevent empty order
    if cart.items.count() == 0:
        return redirect('cart_view')

    # move from Cart -> Pending
    cart.status = 'Pending'
    cart.save()

    return redirect('orders_history')

@login_required
def orders_history(request):
    orders = Order.objects.filter(user=request.user).exclude(status='Cart').order_by('-created_at')
    return render(request, 'orders/history.html', {'orders': orders})


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if order.status == 'Pending':
        order.status = 'Cancelled'
        order.save()

    return redirect('orders_history')