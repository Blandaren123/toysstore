from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KiMyNIT1ty1Isx7mPgxn2posvOHRMN5XAnn31KhTtJwSEHU5Ca5I8c7NmbYJ2QjIhgLG2s2RExh5HVZZNzlKoGN00ryFRwJ1S',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)