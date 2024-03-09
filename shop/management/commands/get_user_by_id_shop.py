from django.core.management.base import BaseCommand
from shop.models import User


class Command(BaseCommand):
    help = "Get user by ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            self.stdout.write(f'{user}')
        else:
            self.stdout.write('User not found.')
