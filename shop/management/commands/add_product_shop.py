from django.core.management.base import BaseCommand
from shop.models import Product


class Command(BaseCommand):
    help = "Add new product."

    def handle(self, *args, **kwargs):
        product = Product(name='Phone', description='nokia', price=5000.00, amount=15)
        product.save()
        self.stdout.write(f'{product}')
