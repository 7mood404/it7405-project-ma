from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem
from django.contrib.auth.decorators import login_required, user_passes_test

def is_admin(user):
    return user.is_staff


# PUBLIC: View menu (read-only, with search & filter)
def menu_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    items = MenuItem.objects.all()

    if query:
        items = items.filter(name__icontains=query)

    if category:
        items = items.filter(category=category)

    return render(request, 'menu/menu_list.html', {'items': items})


# ADMIN ONLY: Add menu item
@login_required
@user_passes_test(is_admin)
def menu_add(request):
    if request.method == 'POST':
        MenuItem.objects.create(
            name=request.POST['name'],
            category=request.POST['category'],
            price=request.POST['price'],
            description=request.POST['description']
        )
        return redirect('menu_list')

    return render(request, 'menu/menu_add.html')


# ADMIN ONLY: Delete menu item
@login_required
@user_passes_test(is_admin)
def menu_delete(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)
    item.delete()
    return redirect('menu_list')


# PUBLIC: Menu item details + customization
from orders.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

@login_required
def menu_detail(request, item_id):
    item = get_object_or_404(MenuItem, id=item_id)

    if request.method == 'POST':
        # get/create user's active cart
        cart, _ = Order.objects.get_or_create(user=request.user, status='Cart')

        OrderItem.objects.create(
            order=cart,
            item=item,
            order_type=request.POST.get('type'),
            drink=request.POST.get('drink', ''),
            quantity=int(request.POST.get('quantity', 1)),
        )
        return redirect('cart_view')  # we'll make this page now

    return render(request, 'menu/menu_detail.html', {'item': item})