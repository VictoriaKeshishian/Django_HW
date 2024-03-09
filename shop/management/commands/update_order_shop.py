from django.core.management.base import BaseCommand
from shop.models import Order, User, Product


class Command(BaseCommand):
    help = "Update order by ID."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')
        parser.add_argument('--customer_id', type=int, help='New customer ID')
        parser.add_argument('--product_ids', nargs='+', type=int, help='New product IDs')
        parser.add_argument('--total_price', type=float, help='New total price of the order')

    def handle(self, *args, **kwargs):
        order_id = kwargs['order_id']
        order = Order.objects.filter(pk=order_id).first()
        if order is not None:
            if kwargs['customer_id']:
                customer = User.objects.filter(pk=kwargs['customer_id']).first()
                if customer:
                    order.customer = customer
            if kwargs['product_ids']:
                products = Product.objects.filter(pk__in=kwargs['product_ids'])
                if products:
                    order.products.set(products)
            if kwargs['total_price']:
                order.total_price = kwargs['total_price']
            order.save()
            self.stdout.write(f'Order {order_id} updated successfully.')
        else:
            self.stdout.write('Order not found.')
