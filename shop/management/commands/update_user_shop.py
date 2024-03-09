from django.core.management.base import BaseCommand
from shop.models import User


class Command(BaseCommand):
    help = "Update user by ID."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('--name', type=str, help='New name for the user')
        parser.add_argument('--email', type=str, help='New email for the user')
        parser.add_argument('--number', type=str, help='New number for the user')
        parser.add_argument('--address', type=str, help='New address for the user')
        parser.add_argument('--password', type=str, help='New password for the user')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            if kwargs['name']:
                user.name = kwargs['name']
            if kwargs['email']:
                user.email = kwargs['email']
            if kwargs['number']:
                user.number = kwargs['number']
            if kwargs['address']:
                user.address = kwargs['address']
            if kwargs['password']:
                user.password = kwargs['password']

            user.save()
            self.stdout.write(f'User {pk} updated successfully.')
        else:
            self.stdout.write('User not found.')
