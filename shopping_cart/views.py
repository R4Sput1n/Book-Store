from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Cart
from store.models import Books
from accounts.models import OwnedProducts


@login_required
def add_to_cart(request, product_id):
    customer = request.user
    is_in_cart = Cart.objects.filter(customer=customer, product_id=product_id).exists()
    is_owned = OwnedProducts.objects.filter(owner=customer, product_id=product_id).exists()
    product = Books.objects.get(book_id=product_id)
    if is_owned or is_in_cart:
        if is_owned:
            return add_to_cart_fail(request, 'already_owned')
        if is_in_cart:
            return add_to_cart_fail(request, 'already_in_cart')
    item = Cart(customer=customer, product=product)
    item.save()
    return redirect('store_home')


@login_required
def add_and_redirect_to_cart(request, product_id):
    customer = request.user
    is_in_cart = Cart.objects.filter(customer=customer, product_id=product_id).exists()
    is_owned = OwnedProducts.objects.filter(owner=customer, product_id=product_id).exists()
    product = Books.objects.get(book_id=product_id)
    if is_owned or is_in_cart:
        if is_owned:
            return add_to_cart_fail(request, 'already_owned')
        if is_in_cart:
            return add_to_cart_fail(request, 'already_in_cart')
    else:
        item = Cart(customer=customer, product=product)
        item.save()

    return redirect('cart')


@login_required
def cart(request):
    customer = request.user
    products = Cart.objects.filter(customer=customer)
    total = sum([product.product.price for product in products])

    context = {
        'products': products,
        'total': total
    }
    print(products)
    return render(request, 'cart/cart.html', context)


@login_required
def add_to_cart_fail(request, fail_reason):
    context = {'fail_reason': fail_reason}

    return render(request, 'cart/fail.html', context)


@login_required
def delete_from_cart(request, product_id):
    customer = request.user
    item = Cart.objects.filter(customer=customer, product_id=product_id)
    item.delete()

    return redirect('cart')


@login_required
def clear_cart(request):
    if request.method == 'POST':
        customer_id = request.user
        items = Cart.objects.filter(customer_id=customer_id)
        items.delete()
        return redirect('cart')


@login_required
def buy_products(request):
    if request.method == 'POST':
        customer = request.user
        items = Cart.objects.filter(customer_id=customer.id)
        for item in items:
            book_id = item.product.book_id
            book_item = Books.objects.get(book_id=book_id)
            OwnedProducts(product=book_item, owner=customer).save()

    clear_cart(request)
    return redirect('cart')

