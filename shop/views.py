from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from .models import User, Product, Order


def index(request):
    return render(request, 'shop/base.html')


def user_orders(request, user_id, period):
    user = get_object_or_404(User, pk=user_id)

    # Определяем даты начала и конца периода
    end_date = timezone.now()
    if period == 'week':
        start_date = end_date - timedelta(days=7)
    elif period == 'month':
        start_date = end_date - timedelta(days=30)
    elif period == 'year':
        start_date = end_date - timedelta(days=365)

    # Фильтруем заказы по пользователю и времени
    orders = Order.objects.filter(customer=user, date_ordered__range=(start_date, end_date)).order_by('-date_ordered')

    # Получаем уникальные товары из заказов
    unique_products = set()
    for order in orders:
        unique_products |= set(order.products.all())

    return render(request, 'shop/user_orders.html',
                  {'user': user, 'orders': orders, 'unique_products': unique_products, 'period': period})