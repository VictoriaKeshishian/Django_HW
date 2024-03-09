from django.core.management.base import BaseCommand
from shop.models import Order


class Command(BaseCommand):
    help = "Delete order by ID."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        order = Order.objects.filter(pk=order_id).first()
        if order is not None:
            order.delete()
            self.stdout.write(f'Order {order_id} deleted successfully.')
        else:
            self.stdout.write('Order not found.')
