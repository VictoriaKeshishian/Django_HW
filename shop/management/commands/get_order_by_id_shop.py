from django.core.management.base import BaseCommand
from shop.models import Order


class Command(BaseCommand):
    help = "Get order details by ID."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        order = Order.objects.filter(pk=order_id).first()
        if order is not None:
            self.stdout.write(f'Order ID: {order.id}')
            self.stdout.write(f'Customer: {order.customer}')
            self.stdout.write(f'Total Price: {order.total_price}')
            self.stdout.write('Products:')
            for product in order.products.all():
                self.stdout.write(f'- {product.name}')
        else:
            self.stdout.write('Order not found.')
