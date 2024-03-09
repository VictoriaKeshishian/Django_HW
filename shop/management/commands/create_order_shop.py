from django.core.management.base import BaseCommand
from shop.models import Order, User, Product


class Command(BaseCommand):
    help = "Create a new order."

    def add_arguments(self, parser):
        parser.add_argument('customer_id', type=int, help='Customer ID')
        parser.add_argument('product_ids', nargs='+', type=int, help='Product IDs')
        parser.add_argument('total_price', type=float, help='Total price of the order')

    def handle(self, *args, **kwargs):
        customer_id = kwargs['customer_id']
        products_ids = kwargs['product_ids']
        total_price = kwargs['total_price']

        customer = User.objects.filter(pk=customer_id).first()
        if customer is None:
            self.stdout.write('Customer not found.')
            return

        products = Product.objects.filter(pk__in=products_ids)
        if len(products) != len(products_ids):
            self.stdout.write('Some products not found.')
            return

        order = Order.objects.create(customer=customer, total_price=total_price)
        order.products.set(products)
        self.stdout.write(f'Order {order.pk} created successfully.')
