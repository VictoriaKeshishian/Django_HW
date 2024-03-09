from django.core.management.base import BaseCommand
from shop.models import User


class Command(BaseCommand):
    help = "Add new user."

    def handle(self, *args, **kwargs):
        user = User(name='Jack', email='neo@example.com', number='79005558844', address='st.Lenina 50', password='secret')
        user.save()
        self.stdout.write(f'{user}')
